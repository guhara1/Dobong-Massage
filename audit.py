#!/usr/bin/env python3
"""배포 전 SEO 감사 스크립트.

검사 항목:
  1. 타이틀·디스크립션 중복 (전 페이지 고유해야 함)
  2. 디스크립션 길이 50~160자
  3. 색인 페이지 본문 2,000~2,500자 (요금 블록 제외)
  4. 페이지 간 8-gram Jaccard 유사도 < 0.30
  5. 도어웨이 URL 패턴 (지역+역+테마 조합, 숫자 행정동, 출구별 경로)
  6. JSON-LD 파싱 오류
통과 기준: 모든 항목 위반 0건.
"""
import html
import itertools
import json
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PAGES

MIN_CHARS, MAX_CHARS = 2000, 2500
SIM_LIMIT = 0.30


def body_text(body_html: str) -> str:
    t = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def ngrams(text: str, n: int = 8) -> set:
    toks = text.split()
    return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> int:
    errors = []

    # 1. 타이틀·디스크립션 중복
    for field in ("title", "desc"):
        seen = {}
        for p in PAGES:
            v = p[field]
            if v in seen:
                errors.append(f"[중복 {field}] {seen[v]} ↔ {p['path'] or '/'}")
            seen[v] = p["path"] or "/"

    # 2. 디스크립션 길이
    for p in PAGES:
        n = len(p["desc"])
        if not 50 <= n <= 160:
            errors.append(f"[desc 길이 {n}] {p['path'] or '/'}")

    # 3. 색인 페이지 글자수
    for p in PAGES:
        if p.get("noindex"):
            continue
        n = len(body_text(p["body"]))
        if not MIN_CHARS <= n <= MAX_CHARS:
            errors.append(f"[글자수 {n}] {p['path'] or '/'}")

    # 4. 페이지 간 유사도 (색인 페이지만)
    indexed = [p for p in PAGES if not p.get("noindex")]
    grams = {p["path"]: ngrams(body_text(p["body"])) for p in indexed}
    worst = 0.0
    for a, b in itertools.combinations(indexed, 2):
        s = jaccard(grams[a["path"]], grams[b["path"]])
        worst = max(worst, s)
        if s >= SIM_LIMIT:
            errors.append(f"[유사도 {s:.2f}] {a['path'] or '/'} ↔ {b['path'] or '/'}")

    # 5. 도어웨이 URL 패턴
    stations = ("station",)
    themes = ("swedish", "lomilomi", "thai", "chinese", "aroma", "homecare",
              "hotel-style", "foot", "sports", "skincare", "waxing", "couple",
              "24hours", "overnight")
    for p in PAGES:
        path = p["path"]
        if any(s in path for s in stations) and any(f"/{t}" in path or path.rstrip("/").endswith(t) for t in themes):
            errors.append(f"[도어웨이: 역+테마] {path}")
        if re.search(r"-\d+-dong/", path):
            errors.append(f"[도어웨이: 숫자 행정동] {path}")
        if "exit" in path or "chulgu" in path:
            errors.append(f"[도어웨이: 출구별] {path}")

    # 6. JSON-LD 파싱
    for p in PAGES:
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',
                             p.get("extra_head", ""), flags=re.S):
            try:
                json.loads(m.group(1))
            except json.JSONDecodeError as e:
                errors.append(f"[JSON-LD 오류] {p['path'] or '/'}: {e}")

    print(f"검사 페이지: {len(PAGES)}개 (색인 {len(indexed)}개)")
    print(f"페이지 간 최대 유사도: {worst:.3f} (기준 < {SIM_LIMIT})")
    if errors:
        print(f"\n위반 {len(errors)}건:")
        for e in errors:
            print(" -", e)
        return 1
    print("위반 0건 — 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
