#!/usr/bin/env python3
"""
generate_web_indexes.py

CI 빌드 시 Obsidian Dataview 쿼리 기반 _INDEX.md 파일을
정적 마크다운 테이블로 교체하여 Quartz에서 렌더링 가능하게 만듦.

원본 레포의 _INDEX.md는 변경하지 않음 (CI 복사본만 덮어씀).

Usage:
    python generate_web_indexes.py --content-dir quartz/content
    python generate_web_indexes.py --content-dir . --dry-run
"""

import argparse
import os
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Frontmatter 파싱
# ---------------------------------------------------------------------------

def parse_frontmatter(filepath: Path) -> dict:
    """YAML frontmatter를 파싱하여 dict로 반환."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return {}

    if not text.startswith("---"):
        return {}

    end = text.find("---", 3)
    if end == -1:
        return {}

    try:
        fm = yaml.safe_load(text[3:end])
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}


# ---------------------------------------------------------------------------
# 스캐너
# ---------------------------------------------------------------------------

def scan_daily_news(content_dir: Path) -> list[dict]:
    """AI Daily News 디렉토리에서 daily-digest 파일을 스캔."""
    news_dir = content_dir / "AI Daily News"
    if not news_dir.exists():
        return []

    digests = []
    for md in news_dir.rglob("*.md"):
        fm = parse_frontmatter(md)
        if fm.get("type") != "daily-digest":
            continue
        if "_TEMPLATE" in md.name:
            continue

        rel = md.relative_to(content_dir)
        digests.append({
            "date": str(fm.get("date", "")),
            "article_count": fm.get("article_count", 0),
            "community_count": fm.get("community_count", 0),
            "deep_dive_count": fm.get("deep_dive_count", 0),
            "product_mentions": fm.get("product_mentions", []) or [],
            "topic_tags": fm.get("topic_tags", []) or [],
            "status": fm.get("status", ""),
            "rel_path": str(rel.with_suffix("")),  # e.g. "AI Daily News/2026/02/2026-02-12"
        })

    digests.sort(key=lambda d: d["date"], reverse=True)
    return digests


def scan_products(content_dir: Path) -> list[dict]:
    """AI Agent Products 디렉토리에서 product-profile 파일을 스캔."""
    prod_dir = content_dir / "AI Agent Products"
    if not prod_dir.exists():
        return []

    products = []
    for md in prod_dir.rglob("*.md"):
        fm = parse_frontmatter(md)
        if fm.get("type") != "product-profile":
            continue
        if "_TEMPLATE" in md.name:
            continue

        slug = md.parent.name
        tags = [t for t in (fm.get("tags", []) or []) if t != "AI-Agent"]
        products.append({
            "product_name": fm.get("product_name", slug),
            "vendor": fm.get("vendor", ""),
            "category": fm.get("category", ""),
            "tags": tags,
            "status": fm.get("status", ""),
            "last_updated": str(fm.get("last_updated", "")),
            "slug": slug,
            "link": f"[[AI Agent Products/{slug}/{slug}|{fm.get('product_name', slug)}]]",
        })

    category_order = {"B2C": 0, "Enterprise": 1, "Analytics": 2, "Knowledge": 3}
    products.sort(key=lambda p: (category_order.get(p["category"], 99), p["product_name"]))
    return products


def scan_insights(content_dir: Path) -> list[dict]:
    """Insights 디렉토리에서 insight-synthesis 파일을 스캔."""
    ins_dir = content_dir / "Insights"
    if not ins_dir.exists():
        return []

    insights = []
    for md in ins_dir.rglob("*.md"):
        fm = parse_frontmatter(md)
        if fm.get("type") not in ("insight-synthesis", "insight-comparison"):
            continue
        if "_TEMPLATE" in md.name:
            continue

        category = fm.get("category", md.parent.name)
        slug = md.stem
        insights.append({
            "topic_name": fm.get("topic_name", slug),
            "category": category,
            "status": fm.get("status", ""),
            "confidence": fm.get("confidence", ""),
            "last_updated": str(fm.get("last_updated", "")),
            "slug": slug,
            "link": f"[[Insights/{category}/{slug}|{fm.get('topic_name', slug)}]]",
        })

    insights.sort(key=lambda i: i["last_updated"], reverse=True)
    return insights


# ---------------------------------------------------------------------------
# 역할 정보 파싱 (AGENTS.md)
# ---------------------------------------------------------------------------

ROLE_DISPLAY = {
    "frontend_agent": ("개발자 (Frontend)", "UI 컴포넌트 설계, 인터랙션 패턴"),
    "backend_agent": ("개발자 (Backend)", "런타임, 도구 연결, API 설계"),
    "architecture_agent": ("아키텍트", "시스템 아키텍처, 기술 스택 결정"),
    "planning_agent": ("기획자", "요구사항 정의, 기능 스펙"),
    "pm_agent": ("PM / 팀장", "경쟁 분석, 경영진 보고"),
    "qa_agent": ("QA", "테스트 전략, 품질 기준"),
    "data_agent": ("데이터", "데이터 파이프라인, KG 구축"),
    "sales_agent": ("영업/BD", "차별화 포인트, 제안서 작성"),
}


def parse_agents_md(content_dir: Path) -> dict[str, tuple[str, str]]:
    """AGENTS.md에서 각 역할의 첫 번째 primary_source와 설명을 추출.

    Returns: {role_id: (path, description)}
    """
    agents_file = content_dir / "AGENTS.md"
    if not agents_file.exists():
        return {}

    text = agents_file.read_text(encoding="utf-8")
    roles = {}
    current_role = None
    in_primary = False

    for line in text.splitlines():
        role_match = re.match(r"^###\s+(\w+_agent)", line)
        if role_match:
            current_role = role_match.group(1)
            in_primary = False
            continue

        if current_role and "**primary_sources**:" in line:
            in_primary = True
            continue

        if current_role and "**secondary_sources**:" in line:
            in_primary = False
            continue

        if in_primary and current_role not in roles:
            # `  - `Insights/path/file.md` — 설명`
            src_match = re.match(r"\s+-\s+`([^`]+\.md)`\s*—\s*(.+)", line)
            if src_match:
                path = src_match.group(1)
                desc = src_match.group(2).strip()
                roles[current_role] = (path, desc)
                in_primary = False

    return roles


# ---------------------------------------------------------------------------
# 인덱스 생성
# ---------------------------------------------------------------------------

def generate_daily_news_index(digests: list[dict]) -> str:
    """AI Daily News _INDEX.md 생성."""
    lines = [
        "---",
        "title: AI Daily News 인덱스",
        "---",
        "",
        "# AI Daily News 인덱스",
        "",
        "> AI 관련 일일 뉴스 수집 및 요약 현황.",
        "",
        "---",
        "",
    ]

    # 최근 다이제스트 테이블
    lines.append("## 최근 일일 다이제스트")
    lines.append("")

    if digests:
        recent = digests[:14]
        lines.append("| 날짜 | 기사 수 | 커뮤니티 | Deep Dive | 제품 언급 | 상태 |")
        lines.append("|------|---------|---------|-----------|----------|------|")
        for d in recent:
            date_link = f"[[{d['rel_path']}|{d['date']}]]"
            mentions = ", ".join(d["product_mentions"][:5])
            if len(d["product_mentions"]) > 5:
                mentions += f" 외 {len(d['product_mentions']) - 5}건"
            lines.append(
                f"| {date_link} | {d['article_count']} | {d['community_count']} "
                f"| {d['deep_dive_count']} | {mentions} | {d['status']} |"
            )
    else:
        lines.append("아직 수집된 다이제스트가 없습니다.")

    lines.extend(["", "---", ""])

    # 제품별 뉴스 언급 빈도
    lines.append("## 제품별 뉴스 언급 빈도")
    lines.append("")

    product_counter: Counter = Counter()
    for d in digests:
        product_counter.update(d["product_mentions"])

    if product_counter:
        lines.append("| 제품 | 언급 횟수 |")
        lines.append("|------|----------|")
        for product, count in product_counter.most_common():
            lines.append(f"| {product} | {count} |")
    else:
        lines.append("데이터가 없습니다.")

    lines.extend(["", "---", ""])

    # 주제별 뉴스 분포
    lines.append("## 주제별 뉴스 분포")
    lines.append("")

    topic_counter: Counter = Counter()
    for d in digests:
        topic_counter.update(d["topic_tags"])

    if topic_counter:
        lines.append("| 주제 | 언급 횟수 |")
        lines.append("|------|----------|")
        for topic, count in topic_counter.most_common():
            lines.append(f"| {topic} | {count} |")
    else:
        lines.append("데이터가 없습니다.")

    lines.append("")
    return "\n".join(lines)


def generate_products_index(products: list[dict]) -> str:
    """AI Agent Products _INDEX.md 생성."""
    lines = [
        "---",
        "title: AI Agent Products 인덱스",
        "---",
        "",
        "# AI Agent Products 리서치 인덱스",
        "",
        "> AI Agent 서비스별 종합 리서치 현황.",
        "",
        "---",
        "",
    ]

    # 전체 제품 목록
    lines.append("## 전체 제품 목록")
    lines.append("")
    lines.append("| 제품 | 회사 | 분류 | 상태 | 최종 수정 |")
    lines.append("|------|------|------|------|----------|")
    for p in products:
        lines.append(
            f"| {p['link']} | {p['vendor']} | {p['category']} "
            f"| {p['status']} | {p['last_updated']} |"
        )

    lines.extend(["", "---", ""])

    # 카테고리별 섹션
    categories = ["B2C", "Enterprise", "Analytics", "Knowledge"]
    for cat in categories:
        cat_products = [p for p in products if p["category"] == cat]
        if not cat_products:
            continue

        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| 제품 | 회사 | 주요 태그 |")
        lines.append("|------|------|----------|")
        for p in cat_products:
            tags_str = ", ".join(p["tags"][:4])
            lines.append(f"| {p['link']} | {p['vendor']} | {tags_str} |")
        lines.extend(["", "---", ""])

    # 태그 매트릭스
    lines.append("## 태그 매트릭스")
    lines.append("")
    lines.append("| 제품 | 태그 |")
    lines.append("|------|------|")
    for p in products:
        tags_str = ", ".join(p["tags"])
        lines.append(f"| {p['link']} | {tags_str} |")

    lines.append("")
    return "\n".join(lines)


def generate_insights_index(insights: list[dict]) -> str:
    """Insights _INDEX.md 생성."""
    lines = [
        "---",
        "title: Insights 인덱스",
        "---",
        "",
        "# Insights 인덱스",
        "",
        "교차 분석 인사이트 문서를 카테고리별로 탐색합니다.",
        "",
        "---",
        "",
    ]

    # 카테고리별 섹션
    category_info = {
        "agent-skills": "Agent Skills — Skill 개발",
        "agent-runtime": "Agent Runtime — Deep Agent 아키텍처",
        "knowledge-data": "Knowledge & Data — KG 세팅",
        "agent-ui": "Agent UI — UI 개발",
        "protocols": "Protocols — 프로토콜",
        "open-source": "Open Source — 오픈소스",
        "market": "Market — 시장·경쟁",
        "strategy": "Strategy — PM·전략",
        "security-evaluation": "Security & Evaluation — 보안·평가",
        "maintenance": "Maintenance — 유지보수",
    }

    for cat_id, cat_title in category_info.items():
        cat_insights = [i for i in insights if i["category"] == cat_id]
        if not cat_insights:
            continue

        lines.append(f"## {cat_title}")
        lines.append("")
        lines.append("| 주제 | 상태 | 신뢰도 | 최종 수정 |")
        lines.append("|------|------|--------|----------|")
        for i in cat_insights:
            lines.append(
                f"| {i['link']} | {i['status']} | {i['confidence']} | {i['last_updated']} |"
            )
        lines.extend(["", "---", ""])

    # 전체 인사이트 최근 수정순
    lines.append("## 전체 인사이트 (최근 수정순)")
    lines.append("")

    top20 = insights[:20]
    if top20:
        lines.append("| 주제 | 카테고리 | 상태 | 최종 수정 |")
        lines.append("|------|---------|------|----------|")
        for i in top20:
            lines.append(
                f"| {i['link']} | {i['category']} | {i['status']} | {i['last_updated']} |"
            )
    else:
        lines.append("아직 작성된 인사이트가 없습니다.")

    lines.append("")
    return "\n".join(lines)


def generate_homepage(
    digests: list[dict],
    products: list[dict],
    insights: list[dict],
    roles: dict[str, str],
) -> str:
    """index.md (홈페이지) 생성."""
    lines = [
        "---",
        "title: KonaChain AI Research",
        "---",
        "",
        "# KonaChain AI Research",
        "",
        "엔터프라이즈 AI 에이전트 개발을 위한 리서치 허브입니다.",
        "",
        "---",
        "",
    ]

    # 오늘의 다이제스트
    lines.append("## 최근 다이제스트")
    lines.append("")
    if digests:
        lines.append("| 날짜 | 기사 수 | Deep Dive | 주요 제품 |")
        lines.append("|------|---------|-----------|----------|")
        for d in digests[:3]:
            date_link = f"[[AI Daily News/{d['rel_path']}|{d['date']}]]"
            mentions = ", ".join(d["product_mentions"][:4])
            if len(d["product_mentions"]) > 4:
                mentions += " ..."
            lines.append(
                f"| {date_link} | {d['article_count']} | {d['deep_dive_count']} | {mentions} |"
            )
        lines.append("")
        lines.append("[[AI Daily News/_INDEX|전체 다이제스트 목록 >>]]")
    else:
        lines.append("아직 수집된 다이제스트가 없습니다.")

    lines.extend(["", "---", ""])

    # 역할별 바로가기
    lines.append("## 역할별 바로가기")
    lines.append("")
    lines.append("| 역할 | 시작 문서 | 설명 |")
    lines.append("|------|----------|------|")

    for role_id, (display_name, description) in ROLE_DISPLAY.items():
        role_data = roles.get(role_id)
        if role_data:
            source_path, source_desc = role_data
            link = f"[[{source_path.removesuffix('.md')}|{source_desc}]]"
        else:
            link = "—"
        lines.append(f"| **{display_name}** | {link} | {description} |")

    lines.append("")
    lines.append("[[Docs/ONBOARDING|처음 방문하셨나요? 온보딩 가이드 >>]]")

    lines.extend(["", "---", ""])

    # AI Agent Products
    lines.append("## AI Agent Products")
    lines.append("")
    lines.append("19개 AI 에이전트 서비스의 종합 리서치입니다.")
    lines.append("")

    # 카테고리별 제품 목록
    lines.append("| 분류 | 제품 |")
    lines.append("|------|------|")
    categories = ["B2C", "Enterprise", "Analytics", "Knowledge"]
    for cat in categories:
        cat_products = [p for p in products if p["category"] == cat]
        if cat_products:
            product_links = ", ".join(p["link"] for p in cat_products)
            lines.append(f"| **{cat}** | {product_links} |")

    lines.append("")
    lines.append("[[AI Agent Products/_INDEX|전체 제품 인덱스 >>]]")

    lines.extend(["", "---", ""])

    # Insights
    lines.append("## Insights (교차 분석)")
    lines.append("")
    lines.append("제품과 뉴스를 교차 분석한 주제별 인사이트입니다.")
    lines.append("")

    category_display = {
        "agent-skills": ("Agent Skills", "Skill 개발"),
        "agent-runtime": ("Agent Runtime", "Deep Agent"),
        "knowledge-data": ("Knowledge & Data", "KG 세팅"),
        "agent-ui": ("Agent UI", "UI 개발"),
        "protocols": ("Protocols", "전체"),
        "open-source": ("Open Source", "전체"),
        "market": ("Market", "전체"),
        "strategy": ("Strategy", "PM·팀장"),
        "security-evaluation": ("Security & Eval", "전체"),
    }

    lines.append("| 영역 | 문서 수 | 대상 |")
    lines.append("|------|---------|------|")
    for cat_id, (cat_name, target) in category_display.items():
        cat_insights = [i for i in insights if i["category"] == cat_id]
        count = len(cat_insights)
        if cat_insights:
            # 카테고리의 첫 번째 인사이트로 링크
            first = cat_insights[0]
            link = f"[[Insights/{first['category']}/{first['slug']}|{cat_name}]]"
        else:
            link = cat_name
        lines.append(f"| {link} | {count} | {target} |")

    lines.append("")
    lines.append("[[Insights/_INDEX|전체 인사이트 인덱스 >>]]")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate static web indexes for Quartz")
    parser.add_argument("--content-dir", required=True, help="Content directory path")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing files")
    args = parser.parse_args()

    content_dir = Path(args.content_dir).resolve()
    if not content_dir.exists():
        print(f"ERROR: Content directory not found: {content_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning content directory: {content_dir}")

    # 스캔
    digests = scan_daily_news(content_dir)
    print(f"  Found {len(digests)} daily digests")

    products = scan_products(content_dir)
    print(f"  Found {len(products)} product profiles")

    insights = scan_insights(content_dir)
    print(f"  Found {len(insights)} insight documents")

    roles = parse_agents_md(content_dir)
    print(f"  Found {len(roles)} agent roles")

    # 생성
    outputs = {
        content_dir / "AI Daily News" / "_INDEX.md": generate_daily_news_index(digests),
        content_dir / "AI Agent Products" / "_INDEX.md": generate_products_index(products),
        content_dir / "Insights" / "_INDEX.md": generate_insights_index(insights),
        content_dir / "index.md": generate_homepage(digests, products, insights, roles),
    }

    for filepath, content in outputs.items():
        if args.dry_run:
            print(f"\n{'='*60}")
            print(f"FILE: {filepath.relative_to(content_dir)}")
            print(f"{'='*60}")
            print(content)
        else:
            filepath.write_text(content, encoding="utf-8")
            print(f"  Written: {filepath.relative_to(content_dir)}")

    print("\nDone.")


if __name__ == "__main__":
    main()
