#!/usr/bin/env python3
"""IndexNow 즉시 색인 요청 — 네이버·빙 등 IndexNow 참여 검색엔진에 URL 변경을 통지한다.

사용법 (배포 후 실행):
  python3 indexnow.py            # sitemap.xml 의 전체 URL 제출
  python3 indexnow.py URL [URL…] # 특정 URL만 제출

구글은 IndexNow 를 사용하지 않으므로 Search Console 의 사이트맵 제출과
URL 검사(색인 생성 요청)를 함께 사용해야 한다.
주의: BASE_URL 이 실제 배포 도메인으로 설정·배포된 뒤에 실행할 것.
키 파일({KEY}.txt)이 사이트 루트에서 응답해야 검증이 통과된다.
"""
import json
import re
import sys
import urllib.request

sys.path.insert(0, ".")
from content.site import BASE_URL

KEY = "dc15b530a6d14855ba84c962710f017f"
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls() -> list:
    with open("sitemap.xml", encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main() -> int:
    base = BASE_URL.rstrip("/")
    if "example.com" in base:
        print("BASE_URL 이 아직 플레이스홀더입니다. content/site.py 를 실제 도메인으로 바꾼 뒤")
        print("python3 build.py 를 재실행하고 배포한 다음 이 스크립트를 실행하세요.")
        return 1

    urls = sys.argv[1:] or sitemap_urls()
    host = base.split("//", 1)[1]
    payload = {
        "host": host,
        "key": KEY,
        "keyLocation": f"{base}/{KEY}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req) as res:
        print(f"{len(urls)}개 URL 제출 — HTTP {res.status} (200/202 = 접수 완료)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
