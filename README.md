# 스피드 마사지 — 도봉 출장마사지·홈타이 안내 사이트

도봉구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ LocalBusiness/FAQPage JSON-LD)
  areas.py          # 지역별: 도봉구 허브 + 대표 동 4개
  stations.py       # 지하철역별: 허브 + 6개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 허브 + 아티클 6편 (Article JSON-LD)
  about.py          # 운영자 소개 (E-E-A-T)
assets/             # CSS, 모바일 내비 JS, 파비콘·OG 이미지
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 4개만 (쌍문동·방학동·창동·도봉동) — 숫자 행정동 페이지 없음
  - 쌍문1~4동 → 쌍문동 / 방학1~3동 → 방학동 / 창1~5동 → 창동 / 도봉1~2동 → 도봉동
- 역은 역 1개당 페이지 1개 (쌍문역·창동역·녹천역·방학역·도봉역·도봉산역) —
  창동역(1·4호선)·도봉산역(1·7호선) 환승역도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 상단/하위 메뉴와 푸터에 키워드·지역명·역명 대량 나열 없음
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·rss·robots.txt에 반영됨)
3. HTTPS 활성화 후 배포

## 빠른 색인(인덱싱) 등록 절차

빌드가 자동 생성하는 색인 파일:

- `sitemap.xml` — 색인 42페이지 전체 + `lastmod` (재수집 판단 신호)
- `rss.xml` — 매거진 아티클 피드 (네이버는 사이트맵·RSS 병행 제출 권장)
- `robots.txt` — 전체 허용 + Googlebot·Yeti(네이버) 명시 + 사이트맵·RSS 위치 등록
- 전 페이지 `<head>`에 RSS 자동발견 링크 포함

### 구글 (Search Console)

1. 속성 등록 후 `sitemap.xml` 제출 (Sitemaps 메뉴)
2. 메인·지역 허브 등 핵심 URL은 "URL 검사 → 색인 생성 요청"으로 개별 요청
3. 구글은 IndexNow를 사용하지 않으므로 위 두 가지가 전부다

### 네이버 (서치어드바이저)

1. 소유 확인 — 메인 페이지에 확인 메타 태그 이미 포함됨
2. 요청 → 사이트맵 제출에 `sitemap.xml`, RSS 제출에 `rss.xml` 등록
3. 핵심 URL은 "요청 → 웹 페이지 수집"으로 개별 수집 요청 (일일 한도 내)

### IndexNow (네이버·빙 즉시 통지)

배포 후 한 번 실행하면 사이트맵의 전체 URL 변경 사실을 즉시 통지한다:

```bash
python3 indexnow.py                # sitemap.xml 전체 URL 제출
python3 indexnow.py https://…/url/ # 특정 URL만 제출
```

키 파일(`dc15b530a6d14855ba84c962710f017f.txt`)이 사이트 루트에 함께 배포되어야
검증이 통과된다. 콘텐츠를 수정·재배포할 때마다 다시 실행하면 된다.
