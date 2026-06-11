# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = """<meta name="naver-site-verification" content="a373b22c0b0b3318177e23376ba13f0753e0080e" />
""" + f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "도봉구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 도봉구"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "도봉구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "기본 범위는 도봉구 전체입니다. 다만 같은 주소라도 시간대와 배정 상황에 따라 달라질 수 있으니, 쌍문동·방학동·창동·도봉동 각 페이지를 본 뒤 전화로 확정하시는 것이 정확합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "창동역이나 쌍문역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능합니다. 여섯 개 역세권은 각 역 페이지에서 주변 생활권과 함께 다루고 있으며, 실제 가능 여부는 예약 시 말씀해 주시는 위치를 기준으로 확인해 드립니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "쌍문1동과 쌍문2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "숫자 행정동은 생활권이 같아서 페이지를 나누면 내용이 중복되기 때문입니다. 쌍문1동부터 4동까지는 쌍문동 페이지 한 곳에서 모두 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "낮 시간대라면 당일도 어렵지 않은 편입니다. 저녁과 주말은 문의가 몰려 대기가 생길 수 있으니 미리 연락 주시기를 권합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "테마별 안내에 열네 가지 유형을 정리해 두었습니다. 스웨디시, 타이마사지, 홈케어 등 각 페이지에서 특징과 잘 맞는 분을 확인하실 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 도봉구 전지역</p>
    <h1>도봉 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">이동할 필요 없이 머무시는 곳에서 받는 프리미엄 방문 관리.<br>자택이든 오피스텔이든 숙소든, 전화 한 통으로 예약이 마무리됩니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>4개</strong><span>대표 지역</span></li>
      <li><strong>6개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>도봉 출장마사지·홈타이 서비스 안내</h2>
<p>도봉구에서 방문 마사지나 홈타이를 알아보고 계신다면 이 페이지부터 보시면 됩니다. 방문 가능 지역, 예약 순서, 코스 선택 기준, 방문 전 준비까지 큰 틀에서 담았습니다. 메인은 사이트 전체를 잇는 허브이고, 깊이 있는 설명은 지역별·지하철역별·테마별 페이지가 맡습니다. {BRAND}는 상담 전화에서 들으신 안내와 실제 방문이 어긋나지 않도록 모든 절차를 기록으로 남겨 운영하고 있습니다.</p>
</section>

<section id="coverage">
<h2>도봉구 전지역 방문 가능 안내</h2>
<p>지역 안내의 뼈대는 쌍문동, 방학동, 창동, 도봉동 네 개 대표 동입니다. 행정 구역으로는 쌍문1~4동, 방학1~3동, 창1~5동, 도봉1~2동의 열네 개 행정동으로 나뉘지만, 숫자 동마다 페이지를 따로 두지 않고 대표 동 페이지 하나에 묶어 설명합니다. 동일한 생활권을 숫자 단위로 쪼개면 내용이 겹치는 페이지만 늘어나기 때문에, 생활권 단위로 묶는 쪽이 찾는 분께도 명확합니다.</p>
</section>

<section id="areas">
<h2>지역별 안내</h2>
<p>아래 네 개 동 페이지에는 그 동네만의 생활권 이야기가 담겨 있습니다. 주거 형태와 골목 사정, 가까운 역, 자주 들어오는 예약 상황, 방문이 매끄러운 시간대까지 동마다 다른 내용으로 정리했으니, 거주지나 머무시는 곳에 해당하는 동을 골라 확인해 주세요.</p>
<ul class="card-grid">
<li><a href="/dobong-gu/ssangmun-dong/">쌍문동</a></li>
<li><a href="/dobong-gu/banghak-dong/">방학동</a></li>
<li><a href="/dobong-gu/chang-dong/">창동</a></li>
<li><a href="/dobong-gu/dobong-dong/">도봉동</a></li>
</ul>
<p>네 개 동이 어떻게 나뉘고 묶이는지 전체 그림은 <a href="/dobong-gu/">도봉구 전체 안내</a>에 담아 두었습니다.</p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>도봉구에는 1호선과 4호선, 7호선이 지나며 안내 기준이 되는 역은 여섯 곳입니다. 역 페이지마다 역세권 분위기, 닿아 있는 대표 동, 방문 전 준비할 점을 담았습니다. 창동역(1·4호선)과 도봉산역(1·7호선)은 환승역이지만 페이지와 주소는 하나만 운영하고, 출구 단위 페이지나 역과 테마를 엮은 페이지는 두지 않습니다.</p>
<ul class="card-grid">
<li><a href="/dobong-gu/stations/ssangmun-station/">쌍문역</a></li>
<li><a href="/dobong-gu/stations/chang-dong-station/">창동역</a></li>
<li><a href="/dobong-gu/stations/nokcheon-station/">녹천역</a></li>
<li><a href="/dobong-gu/stations/banghak-station/">방학역</a></li>
<li><a href="/dobong-gu/stations/dobong-station/">도봉역</a></li>
<li><a href="/dobong-gu/stations/dobongsan-station/">도봉산역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>관리 유형은 열네 가지 테마로 나누어 안내합니다. 각 테마 페이지에서 기법의 특징, 잘 맞는 분, 받기 전에 확인할 점을 다루며, 어떤 테마든 도봉구 어느 동·어느 역에서나 같은 조건으로 예약할 수 있습니다. 그래서 역 이름과 테마를 엮은 조합 페이지는 만들지 않습니다. 테마를 먼저 정하시고 위치는 전화로 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>시간과 구성은 그날의 몸 상태를 기준으로 고르는 것이 가장 자연스럽습니다. 뭉침이 심하게 쌓인 날, 조용한 휴식이 필요한 날, 운동 직후의 회복, 숙소에서의 이용, 두 사람 동시 진행처럼 상황별로 어떤 코스가 어울리는지 <a href="/courses/">코스안내</a>에 기준을 정리해 두었습니다. 애매하다면 전화에서 상태만 말씀해 주셔도 됩니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>전화 한 통이면 위치 확인, 시간 확인, 코스·인원 확인, 가능 여부 안내, 확정까지 다섯 단계가 한 번에 끝납니다. 평일 저녁과 주말 밤은 배정이 빨리 차는 시간대라, 받고 싶은 시각보다 한두 시간 앞서 연락 주시는 편이 좋습니다. 단계마다 무엇을 묻고 안내하는지는 <a href="/reservation/">예약안내</a>에 자세히 풀어 두었습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>방문 전에는 도로명 주소, 공동현관 출입 방법, 차량 진입과 주차 여부, 관리받을 공간이 조용한지를 한 번씩 점검해 주세요. 오피스텔이나 숙소라면 건물 출입 절차와 예약 시간대에 연락이 닿는 번호를 함께 알려주시면 도착 시간이 정확해집니다. 전체 점검 목록은 <a href="/guide/">이용가이드</a>를 참고하시면 됩니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>모든 관리는 공개된 위생 기준과 안내된 서비스 범위 안에서만 진행됩니다. 예약 정보는 방문 조율 외의 용도로 쓰지 않고 개인정보는 정해진 기준에 따라 처리하며, 범위를 벗어나는 요청이나 불법적인 요청은 어떤 경우에도 받지 않습니다. 이 기준은 상담부터 방문 종료까지 동일하게 적용됩니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>도봉구 전지역 방문이 가능한가요?</h3>
<p>기본 범위는 도봉구 전체입니다. 다만 같은 주소라도 시간대와 배정 상황에 따라 달라질 수 있으니, 쌍문동·방학동·창동·도봉동 각 페이지를 본 뒤 전화로 확정하시는 것이 정확합니다.</p>
</div>
<div class="faq-item">
<h3>창동역이나 쌍문역 근처도 가능한가요?</h3>
<p>가능합니다. 여섯 개 역세권은 각 역 페이지에서 주변 생활권과 함께 다루고 있으며, 실제 가능 여부는 예약 시 말씀해 주시는 위치를 기준으로 확인해 드립니다.</p>
</div>
<div class="faq-item">
<h3>쌍문1동과 쌍문2동은 왜 따로 없나요?</h3>
<p>숫자 행정동은 생활권이 같아서 페이지를 나누면 내용이 중복되기 때문입니다. 쌍문1동부터 4동까지는 쌍문동 페이지 한 곳에서 모두 안내합니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>낮 시간대라면 당일도 어렵지 않은 편입니다. 저녁과 주말은 문의가 몰려 대기가 생길 수 있으니 미리 연락 주시기를 권합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>테마별 안내에 열네 가지 유형을 정리해 두었습니다. 스웨디시, 타이마사지, 홈케어 등 각 페이지에서 특징과 잘 맞는 분을 확인하실 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>위치와 희망 시간, 두 가지만 준비되면 상담은 길지 않습니다. 전화 주시면 도봉구 내 가능 여부를 그 자리에서 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "도봉 출장마사지·홈타이 | 도봉구 전지역 방문 마사지 예약 안내",
    "desc": "도봉 출장마사지·홈타이 안내 페이지입니다. 쌍문동, 방학동, 창동, 도봉동과 도봉구 주요 지하철역 인근, 테마별 관리, 예약 전 확인사항을 확인해보세요.",
    "h1": "도봉 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
