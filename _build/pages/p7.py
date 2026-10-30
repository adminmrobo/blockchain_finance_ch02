LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '2-07', 'slug': 'difficulty-and-confirmation', 'key': '2_07', 'anchor': 'C',
 'tab_title': '난이도와 확정', 'meta_title': '난이도와 확정 — 몇 블록을 기다려야 안심할까',
 'description': '계산력이 바뀌어도 블록 간격을 지키는 난이도 조정을 실험하고, 백서의 공격자 성공 확률 식으로 몇 블록을 기다려야 거래를 믿을 수 있는지 계산하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.28; Nakamoto (2008) 4·7·11절',
 'h1': '난이도와 확정<br>— 몇 블록을 기다려야 안심할까', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '장비가 늘어나도 블록은 왜 일정한 간격으로 나올까? 송금을 받은 뒤 몇 블록을 기다리면 되돌려질 걱정이 없을까?',
 'lead': '2-06에서 두 가지가 남았습니다. 장비가 늘면 블록이 점점 빨리 나온다는 것, 그리고 계산력을 모은 위조자가 사슬을 다시 쓸 수 있다는 것. 2장의 마지막 편에서는 난이도 조정으로 블록 간격을 지키는 원리를 실험하고, 백서 11절의 식으로 "블록 몇 개를 기다리면 되돌려질 확률이 얼마로 줄어드는지" 직접 계산합니다.',
 'kpis': [('난이도 조정', '참여 장비가 늘면 올리고 줄면 내림', 'a', [1]), ('가장 긴 사슬', '노드가 옳다고 보는 사슬', 'g', [2]), ('0.0002428', 'q=0.1, 6블록 뒤 공격 성공 확률 (백서 표)', 'm', [2]), ('z=5', 'q=0.1에서 확률 0.1% 미만에 필요한 블록 (백서)', 'r', [2])],
 'hero': [('doc', 'think', 'doc_e09', '위조자가 따라잡으려면 정직한 사슬보다 빨리 블록을 쌓아야 해요. 뒤처진 거리가 길수록 가능성은 빠르게 줄어요.'),
          ('asst', 'smile', 'asst_e13', '백서에 실린 계산 코드를 그대로 옮겨서 확률을 계산해요. 백서 표와 맞는지도 제가 대조할게요.'),
          ('fly', 'point', 'fly_e08', '블록 하나 붙었으면 끝난 거 아냐? 왜 자꾸 기다리래?'),
          ('robo', 'coin', 'robo_e16', '블록 하나면 충분하지. 기다리는 시간도 돈이에요!')],
 'cast': [('doc', 'front', 'doc_e08'
           , '해설과 판정.'), ('asst', 'smile', 'asst_e13', '확률을 계산하고 백서 표와 대조한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 6블록을 기다린다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 1블록이면 된다고 본다.')],
 'why_title': '왜 난이도와 확정인가',
 'why_lead': '채굴이 블록 쓰기에 값을 매겼다면(2-06), 이제 그 값을 일정하게 유지하고, 그 값이 쌓인 만큼 거래를 믿는 규칙이 필요해요.',
 'why': [('일정한 블록 간격', '비트코인은 네트워크에 동원된 컴퓨팅 파워를 바탕으로 채굴 난이도를 조정해 정해진 시간에 일정 수의 블록이 생성되게 한다. 장비가 적으면 낮추고 늘면 높인다. <sup>[1]</sup>'),
         ('가장 긴 사슬', '백서는 다수의 결정을 작업증명이 가장 많이 들어간 가장 긴 사슬로 나타내고, 정직한 노드가 계산력 과반을 쥐면 정직한 사슬이 가장 빨리 자란다고 쓴다. <sup>[2]</sup>'),
         ('기다릴수록 안전', '공격자가 z블록 뒤처진 상태에서 따라잡을 확률은 z가 늘수록 지수적으로 줄어든다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: "확정"은 스위치가 아니라 확률이에요. 블록이 쌓일수록 되돌릴 확률이 줄어들 뿐이에요.'),
 'big_lead': '채굴(2-06)의 비용이 위조를 얼마나 어렵게 만드는지 숫자로 닫는 칸입니다. 2장의 마지막이고, 3장 「비트코인」으로 넘어가는 다리이기도 합니다.',
 'ladder': [('①', '난이도 조정', '계산력이 바뀌어도 블록 간격을 목표에 맞춘다', '계산력 과반을 쥔 위조자는 막지 못한다'),
            ('②', '확정 깊이와 공격 확률', 'z블록을 기다리면 공격 성공 확률이 지수적으로 줄어든다', 'q ≥ 0.5이면 기다려도 소용없다 → 3장 51% 공격')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '난이도 조정', 'title': '장비가 늘어도 간격은 그대로 — 난이도 조정',
   'tags': [('방식: 지난 블록들의 평균 간격으로 난이도를 다시 정함', 'g'), ('장부: 쪽을 붙이는 속도를 맞추는 자물쇠 자릿수', '')],
   'left': '<p>쪽을 붙이려면 자물쇠를 열어야 한다. 자물쇠 여는 사람이 늘어 쪽이 너무 빨리 붙으면, 관리인은 다음부터 자물쇠 자릿수를 늘린다. 사람이 줄어 너무 느려지면 자릿수를 줄인다. 그래서 쪽은 늘 비슷한 속도로 붙는다.</p>',
   'right': '<p>참여 장비가 적으면 난이도가 낮아지고, 늘어나면 높아진다. <sup>[1]</sup> 백서는 하드웨어 속도와 참여 관심의 변화를 보정하려고 시간당 평균 블록 수를 목표로 하는 이동 평균으로 난이도를 정하고, 블록이 너무 빨리 만들어지면 난이도를 올린다고 쓴다. <sup>[2]</sup> 백서의 저장 공간 계산은 블록이 10분마다 생성된다고 가정한다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 계산력이 바뀌는 30구간 (구간마다 블록 50개)</h3>
    <div class="cwrap"><canvas id="c1" aria-label="구간별 평균 블록 간격을 난이도 조정이 있을 때와 없을 때로 비교한 선그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">10구간째 계산력 변화</span><input type="range" id="r1j" min="-75" max="300" step="25" value="200" aria-label="10구간째 계산력 변화 퍼센트"><span class="val" id="v1j">200</span>%</div>
      <div class="group"><span class="glabel">이후 구간마다 증가</span><input type="range" id="r1g" min="0" max="10" step="1" value="3" aria-label="구간마다 계산력 증가율"><span class="val" id="v1g">3</span>%</div>
      <div class="group"><button class="bt" id="b1Adj" aria-pressed="true">난이도 조정 켬</button></div></div>
    <h3>행동으로 보기 — 시간축 위에 블록이 붙는 간격</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="같은 시간 동안 조정 없음과 조정 있음 두 사슬에 블록이 붙는 간격을 비교하는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 간격 = 난이도 ÷ 계산력</h4>
    <ol><li>평균 블록 간격은 난이도에 비례하고 계산력에 반비례한다. 계산력이 3배가 되면 조정이 없을 때 간격이 1/3로 줄어든다.</li>
      <li>조정은 지난 구간의 평균 간격을 보고 난이도에 "목표 간격 ÷ 실제 간격"을 곱한다. 한 구간 늦게 따라가지만 곧 목표로 돌아온다.</li>
      <li>블록 간격이 일정하면 블록 수가 곧 시간이 되고, 위조자에게 필요한 계산량도 예측할 수 있다. 다음 칸의 확률 계산은 이 성질을 쓴다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 난이도는 모두에게 똑같이 오른다. 위조자의 계산력 몫은 그대로다. 그럼 위조자는 얼마나 따라잡을 수 있나? → 확정 깊이.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>구간 k의 평균 간격 T<sub>k</sub> = 10분 × D<sub>k</sub> ÷ H<sub>k</sub> (D: 난이도, H: 계산력, 처음 D = H = 1). 조정 규칙: D<sub>k+1</sub> = D<sub>k</sub> × 10 ÷ T̂<sub>k</sub>, T̂<sub>k</sub>는 구간 k에 실제로 나온 블록 50개의 평균 간격(지수분포 난수, 시드 27).</p><p class="lim">구간 길이(블록 50개)와 계산력 변화는 예시값이다. 실제 비트코인의 조정 주기와 한 번에 바꿀 수 있는 폭은 3장에서 다룬다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '조정을 끄니까 간격이 3분대로 떨어지네. 켜면 한 구간 뒤에 다시 10분 근처로 돌아오고.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '확정 깊이', 'title': '몇 블록을 기다릴까 — 공격자가 따라잡을 확률',
   'tags': [('방식: 백서 11절의 공격자 성공 확률 P(q, z)', 'g'), ('장부: 내 거래 뒤에 쌓인 쪽 수', '')],
   'left': '<p>내 거래가 적힌 쪽 뒤에 쪽이 z장 더 붙었다. 위조자가 내 거래를 지운 다른 장부를 몰래 쓰고 있다면, 그 장부가 정직한 장부보다 길어져야 사람들이 그쪽을 믿는다. 위조자가 손이 느릴수록, 뒤처진 쪽이 많을수록 따라잡기는 어렵다.</p>',
   'right': '<p>노드는 언제나 가장 긴 사슬을 옳다고 보고 그 사슬을 늘린다. <sup>[2]</sup> 백서 11절은 정직한 노드가 다음 블록을 찾을 확률을 p, 공격자를 q라 두고, z블록 뒤처진 공격자가 언젠가 따라잡을 확률을 계산한다. p ≤ q이면 확률은 1이고, p &gt; q이면 z가 늘수록 지수적으로 줄어든다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 공격자 몫 q와 기다린 블록 z</h3>
    <div class="cwrap"><canvas id="c2" aria-label="기다린 블록 수 z에 따른 공격 성공 확률을 로그 눈금 선그래프로 그리고 백서 표의 값을 점으로 표시한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">공격자 계산력 몫 q</span><input type="range" id="r2q" min="5" max="55" step="5" value="10" aria-label="공격자 계산력 몫 퍼센트"><span class="val" id="v2q">10</span>%</div>
      <div class="group"><span class="glabel">기다린 블록 z</span><input type="range" id="r2z" min="0" max="12" step="1" value="6" aria-label="기다린 블록 수"><span class="val" id="v2z">6</span>개</div></div>
    <h3>행동으로 보기 — 정직한 사슬과 몰래 쓰는 사슬의 경주</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="정직한 사슬과 공격자 사슬이 각자 계산력 몫에 따라 블록을 붙이며 경주하는 장면"></canvas></div>
    <div class="ctrl"><div class="group"><button class="bt primary" id="b2Race">▶ 경주 다시 보기</button></div></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 도박꾼의 파산 문제</h4>
    <ol><li>정직한 사슬과 공격자 사슬의 길이 차이는 블록마다 +1 또는 −1로 움직인다. 백서는 이를 도박꾼의 파산 문제로 본다.</li>
      <li>z블록 뒤처진 공격자가 언젠가 따라잡을 확률은 (q/p)<sup>z</sup>. 그 사이 공격자가 몰래 쌓은 블록 수를 포아송 분포로 더해 최종 확률 P(q, z)를 얻는다.</li>
      <li>q = 0.1이면 z = 6에서 0.0002428, q = 0.3이면 같은 0.1% 미만을 위해 24블록이 필요하다. 공격자가 셀수록 더 오래 기다려야 한다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> q가 0.5 이상이면 아무리 기다려도 확률은 1이다. 이 "51% 공격"과, 채굴 보상이 공격 대신 정직한 채굴을 택하게 만드는 이유는 3장 「비트코인」에서.</p>''',
   'extra': '<details class="math"><summary>백서의 계산 코드를 옮긴 식</summary><p>λ = z × q/p. P(q, z) = 1 − Σ<sub>k=0..z</sub> [ e<sup>−λ</sup>λ<sup>k</sup>/k! × (1 − (q/p)<sup>z−k</sup>) ]. 이 페이지는 백서 11절의 C 코드(AttackerSuccessProbability)를 자바스크립트로 그대로 옮겨 계산하고, 백서 표의 값과 대조한다.</p><p class="lim">이 모형은 공격자가 처음부터 블록을 몰래 쌓기 시작했고, 정직한 블록이 평균 시간대로 나온다고 가정한다. 네트워크 지연은 무시한다.</p></details><div class="bridge field"><h4>현장에 옮기면 — 금액에 맞춰 기다리기</h4><p>커피 한 잔과 집 한 채를 같은 확정 깊이로 받을 이유는 없다. 백서의 식은 "공격자가 계산력의 몇 %를 쥘 수 있다고 볼지"와 "되돌려질 확률을 얼마까지 견딜지"를 정하면 기다릴 블록 수를 알려 준다. 블록 간격이 일정하니 블록 수는 곧 기다릴 시간이다(①칸).</p></div>',
   'say': ('asst', 'e10', 'asst_e10', 'q = 0.1에서 계산한 값이 백서 표와 일곱째 자리까지 같아요. z가 하나 늘 때마다 확률이 약 4분의 1로 줄어요.')},
 ],
 'duel': {'title': '1블록 확정 vs 6블록 확정',
  'intro': '공격자가 계산력의 10%(q = 0.1)를 쥐고 있다. 초파리는 송금이 담긴 블록 뒤에 6블록이 쌓일 때까지, Money-Robo는 1블록만 기다린 뒤 물건을 내준다. 판정 기준은 <b>공격 성공 확률 P(q, z)</b>(낮을수록 좋음). 위 실험과 같은 함수로 계산한다.',
  'fly': ('z = 6', '한 블록은 너무 얇아. 여섯 블록은 쌓여야지.', '기다린 블록 6개'),
  'robo': ('z = 1', '블록 하나 붙었으면 끝! 기다림은 비용이에요.', '기다린 블록 1개'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>P(0.1, 6)과 P(0.1, 1)을 백서 11절의 식으로 계산한다. 막대는 로그 눈금(10<sup>−5</sup>에서 1까지)이다. 백서 표의 값은 각각 0.0002428, 0.2045873이다.</p><p class="lim">기다리는 시간의 비용(손님을 붙잡아 두는 일)은 판정에 넣지 않았다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>남아 있던 질문</th><th>이번 편의 답</th></tr></thead><tbody>
   <tr><td>장비가 늘면 블록이 빨라진다 (2-06)</td><td>지난 블록들의 평균 간격으로 난이도를 다시 정해 간격을 목표에 맞춘다</td></tr>
   <tr><td>위조자가 사슬을 다시 쓸 수 있다 (2-03)</td><td>뒤처진 블록이 z개면 따라잡을 확률이 지수적으로 줄어든다. 블록을 기다리는 만큼 안전해진다</td></tr>
   <tr><td>몇 블록을 기다리나</td><td>공격자 몫과 견딜 확률로 정한다. q = 0.1, 0.1% 미만이면 5블록, q = 0.3이면 24블록</td></tr></tbody></table></div>
   <h3>2장을 한 줄씩 <span class="stampnote">2장 정리</span></h3>
   <div class="tw"><table class="tb"><thead><tr><th>편</th><th>한 줄</th></tr></thead><tbody>
   <tr><td>2-01 블록</td><td>거래를 묶고, 머리글에 요약을 담는다</td></tr>
   <tr><td>2-02 해시</td><td>어떤 데이터든 고정 길이 지문으로 바꾼다</td></tr>
   <tr><td>2-03 해시 사슬</td><td>이전 블록 지문을 담아 고치면 뒤가 모두 어긋난다</td></tr>
   <tr><td>2-04 DB가 아닌 이력</td><td>현재 값 대신 모든 변경을 남긴다. 빠르기는 DB가 낫다</td></tr>
   <tr><td>2-05 이력 관리 사례</td><td>단계마다 기록하면 중간 바꿔치기가 드러난다</td></tr>
   <tr><td>2-06 채굴</td><td>블록 쓰기에 계산 비용을 매기고, 계산력 몫이 곧 표다</td></tr>
   <tr><td>2-07 난이도와 확정</td><td>간격을 지키고, 블록이 쌓일수록 되돌릴 확률이 줄어든다</td></tr></tbody></table></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '2장은 여기까지예요. 블록과 해시로 장부를 묶었고, 채굴로 다시 쓰기에 값을 매겼고, 확률로 기다릴 만큼을 정했어요. 3장은 이 모두를 쓰는 비트코인 자체예요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'sigh', 'robo_e20'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, Money-Robo가 식은땀을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 난이도 조정은 계산력이 바뀌어도 블록 간격을 목표에 맞춘다.<br>· 노드는 가장 긴 사슬을 믿고, 뒤처진 공격자가 따라잡을 확률은 기다린 블록 수에 지수적으로 줄어든다.<br>· q가 0.5 이상이면 기다려도 소용없다.'),
           ('fly', 'arms', 'fly_e16', '여섯 블록 기다리니 0.02%. 한 블록이면 20%야. 기다리는 게 비용이라도 이건 싸게 먹혀.'),
           ('robo', 'sigh', 'robo_e20', '다섯 번에 한 번꼴로 털릴 뻔했네… 이번 판은 손절.'),
           ('asst', 'e16', 'asst_e16', '2장 대결 집계는 초파리 4승(실격승 1번 포함), Money-Robo 3승이에요. 다음 저장소는 3장 「비트코인」, 51% 공격과 보상 구조를 봐요.')],
 'kg_hint': '난이도, 확정, 가장 긴 사슬, 공격 확률…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.28 (컴퓨팅 파워에 따른 채굴 난이도 조정, 정해진 시간에 일정 수의 블록, 참여 장비에 따라 난이도 증감). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 4절(가장 긴 사슬, 정직한 계산력 과반, 시간당 평균 블록 수를 목표로 한 이동 평균 난이도), 5절(노드는 가장 긴 사슬을 옳다고 봄), 7절(블록이 10분마다 생성된다는 가정), 11절(공격자 성공 확률 식, C 코드, q = 0.1·0.3 표, P &lt; 0.001에 필요한 z). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['난이도 조정 실험의 계산력 변화(10구간째 +200%, 이후 구간마다 +3%)와 구간 길이(블록 50개), 시드 27', '경주 장면의 블록 생성 순서 (시드 고정, 설명용)', '대결: q = 0.1에서 z = 6 대 z = 1 (확률 값은 백서 식으로 계산)'],
 'gloss_keys': [('채굴 난이도', True), ('확정', True), ('가장 긴 사슬', True), ('계산력', False), ('작업증명', False), ('블록', False)],
 'gloss_anchor': {'채굴 난이도': '#lv1', '확정': '#lv2', '가장 긴 사슬': '#lv2', '계산력': '#lv1', '작업증명': '#why', '블록': '#lv1'},
 'quiz': {
  'lv1': [{'q': '난이도를 그대로 두고 참여 계산력만 2배가 되면 평균 블록 간격은?', 'o': ['2배로 길어진다', '그대로다', '절반으로 줄어든다', '4분의 1로 줄어든다'], 'a': 2, 'why': '간격 = 난이도 ÷ 계산력. 계산력이 2배면 간격은 절반이에요.', 'hint': '조정을 끈 선.', 'c': 'lab:concept/mining-difficulty'},
          {'q': '교안이 설명한 난이도 조정의 목적은?', 'o': ['정해진 시간에 일정 수의 블록이 생성되게 하려고', '채굴자 수를 줄이려고', '거래 수수료를 올리려고', '해시 길이를 늘리려고'], 'a': 0, 'why': '장비가 적으면 낮추고, 늘면 높여서 블록 생성 속도를 맞춰요. 교안 p.28.', 'hint': '"일정한 블록 간격" 카드.', 'c': 'lab:method/difficulty-retarget'}],
  'lv2': [{'q': '백서 표에서 q = 0.1, z = 6일 때 공격 성공 확률은?', 'o': ['0.2045873', '0.0002428', '0.5', '0'], 'a': 1, 'why': '6블록을 기다리면 약 0.02%로 줄어요. 0.2045873은 z = 1의 값이에요.', 'hint': '대결의 초파리 쪽 값.', 'c': 'lab:metric/attacker-success'},
          {'q': '공격자의 계산력 몫 q가 0.5 이상이면?', 'o': ['기다린 블록 수와 관계없이 성공 확률이 1이다', 'z = 6이면 안전하다', 'z = 24면 안전하다', '확률이 0이 된다'], 'a': 0, 'why': '백서 식에서 p ≤ q이면 따라잡을 확률은 1이에요.', 'hint': 'q 슬라이더를 50% 이상으로.', 'c': 'lab:limitation/majority-attacker'}]},
 'kgspec': {
  'ladder': ['lab:method/difficulty-retarget', 'lab:method/confirmation-wait'],
  'about': ['lab:concept/mining-difficulty', 'lab:concept/confirmation-depth', 'lab:concept/longest-chain', 'lab:metric/attacker-success'],
  'nodes': [
   ('lab:method/difficulty-retarget', 'Method', '난이도 조정 (이동 평균)', 'difficulty retargeting', '#lv1', '지난 블록들의 평균 간격을 보고 다음 난이도를 정해 블록 간격을 목표에 맞추는 방식.', 4, [(LEC, '교안 p.28'), (WP, '4절')]),
   ('lab:method/confirmation-wait', 'Method', '확정 깊이만큼 기다리기', 'waiting for confirmations', '#lv2', '거래가 담긴 블록 뒤에 z블록이 쌓일 때까지 기다려 공격 성공 확률을 낮추는 방식.', 4, [(WP, '11절')]),
   ('lab:metric/block-interval', 'Metric', '평균 블록 간격', 'average block interval', '#lv1', '블록과 블록 사이에 걸린 시간의 평균. 백서는 10분을 가정한다.', 3, [(WP, '7절')]),
   ('lab:metric/attacker-success', 'Metric', '공격 성공 확률 P(q, z)', 'attacker success probability', '#lv2', 'z블록 뒤처진 공격자가 계산력 몫 q로 정직한 사슬을 따라잡을 확률.', 4, [(WP, '11절')]),
   ('lab:metric/attacker-share', 'Metric', '공격자 계산력 몫 q', 'attacker hash share q', '#lv2', '다음 블록을 공격자가 찾을 확률. 정직한 쪽은 p = 1 − q.', 3, [(WP, '11절')]),
   ('lab:limitation/same-share', 'Limitation', '난이도는 위조자의 몫을 바꾸지 못함', 'difficulty does not change attacker share', '#lv1', '난이도는 모두에게 똑같이 오르므로 공격자의 계산력 몫은 그대로다.', 3),
   ('lab:limitation/majority-attacker', 'Limitation', '계산력 과반 공격자 (q ≥ 0.5)', 'majority attacker', '#lv2', '공격자 몫이 정직한 쪽 이상이면 기다린 블록 수와 관계없이 따라잡을 확률이 1이다.', 4, [(WP, '11절')]),
   ('lab:analogy/lock-digits', 'Analogy', '자물쇠 자릿수 조절 ↔ 난이도 조정', 'lock digits ~ difficulty', '#lv1', '여는 사람이 늘면 자릿수를 늘리고 줄면 줄여 쪽이 붙는 속도를 맞춘다.', 3),
   ('lab:analogy/pages-behind', 'Analogy', '뒤에 붙은 쪽 수 ↔ 확정 깊이', 'pages behind ~ confirmations', '#lv2', '내 거래 뒤에 쪽이 많이 붙을수록 몰래 쓴 장부가 따라잡기 어렵다.', 3),
   ('lab:question/core', 'Question', '몇 블록을 기다려야 거래를 믿을 수 있을까?', 'How many blocks should we wait?', '#top', None, 3),
   ('lab:question/duel', 'Question', 'q = 0.1에서 1블록과 6블록 확정의 공격 성공 확률은?', 'z=1 vs z=6 at q=0.1', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/mining-difficulty', 'lab:partOf', 'lab:method/difficulty-retarget', '#lv1'),
   ('lab:method/difficulty-retarget', 'lab:evaluatedBy', 'lab:metric/block-interval', '#lv1'),
   ('lab:method/difficulty-retarget', 'lab:hasLimitation', 'lab:limitation/same-share', '#lv1'),
   ('lab:limitation/same-share', 'lab:addressedBy', 'lab:method/confirmation-wait', '#lv2'),
   ('lab:method/difficulty-retarget', 'lab:prerequisiteOf', 'lab:method/confirmation-wait', '#lv2'),
   ('lab:concept/confirmation-depth', 'lab:partOf', 'lab:method/confirmation-wait', '#lv2'),
   ('lab:concept/longest-chain', 'lab:prerequisiteOf', 'lab:method/confirmation-wait', '#lv2'),
   ('lab:method/confirmation-wait', 'lab:evaluatedBy', 'lab:metric/attacker-success', '#lv2'),
   ('lab:metric/attacker-share', 'lab:partOf', 'lab:metric/attacker-success', '#lv2'),
   ('lab:metric/hash-rate', 'lab:broader', 'lab:metric/attacker-share', '#lv2'),
   ('lab:method/confirmation-wait', 'lab:hasLimitation', 'lab:limitation/majority-attacker', '#lv2'),
   ('lab:method/proof-of-work', 'lab:prerequisiteOf', 'lab:concept/longest-chain', '#why'),
   ('lab:concept/block', 'lab:partOf', 'lab:concept/longest-chain', '#lv1'),
   ('lab:metric/attacker-success', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/majority-attacker', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:analogy/lock-digits', 'lab:analogyOf', 'lab:method/difficulty-retarget', '#lv1'),
   ('lab:analogy/pages-behind', 'lab:analogyOf', 'lab:concept/confirmation-depth', '#lv2'),
  ],
  'claims': [
   ('lab:claim/difficulty-adjust', '비트코인은 네트워크에 동원된 컴퓨팅 파워를 바탕으로 채굴 난이도를 조정해 정해진 시간에 일정 수의 블록이 생성되게 하며, 참여 장비가 적으면 낮추고 늘면 높인다', '#why', ['lab:concept/mining-difficulty', 'lab:method/difficulty-retarget'], [(LEC, '교안 p.28')], 'F01'),
   ('lab:claim/moving-average', '난이도는 시간당 평균 블록 수를 목표로 하는 이동 평균으로 정하며, 블록이 너무 빨리 만들어지면 올라간다', '#lv1', ['lab:method/difficulty-retarget'], [(WP, '4절')], 'F02'),
   ('lab:claim/ten-minutes', '백서의 저장 공간 계산은 블록이 10분마다 생성된다고 가정한다', '#lv1', ['lab:metric/block-interval'], [(WP, '7절')], 'F03'),
   ('lab:claim/longest-chain', '다수의 결정은 작업증명이 가장 많이 들어간 가장 긴 사슬로 나타나며, 노드는 가장 긴 사슬을 옳다고 보고 그것을 늘린다', '#why', ['lab:concept/longest-chain'], [(WP, '4·5절')], 'F04'),
   ('lab:claim/exp-decay', 'p > q이면 z블록 뒤처진 공격자가 따라잡을 확률은 z가 늘수록 지수적으로 줄어든다', '#lv2', ['lab:metric/attacker-success', 'lab:concept/confirmation-depth'], [(WP, '11절')], 'F05'),
   ('lab:claim/table-q01', 'q = 0.1에서 공격 성공 확률은 z = 1일 때 0.2045873, z = 6일 때 0.0002428이다', '#duel', ['lab:metric/attacker-success'], [(WP, '11절 표')], 'F06'),
   ('lab:claim/required-z', '확률을 0.1% 미만으로 낮추려면 q = 0.10에서 z = 5, q = 0.30에서 z = 24가 필요하다', '#lv2', ['lab:method/confirmation-wait'], [(WP, '11절 표')], 'F07'),
  ],
  'sims': [('lab:simulation/retarget-30', '난이도 조정 30구간 실험', '#lv1', ['lab:method/difficulty-retarget']),
           ('lab:simulation/attacker-curve', '공격 성공 확률 곡선', '#lv2', ['lab:metric/attacker-success']),
           ('lab:simulation/duel-z1-z6', '1블록 대 6블록 확정 대결', '#duel', ['lab:metric/attacker-success'])],
 },
}
