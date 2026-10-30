LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '2-06', 'slug': 'mining-race', 'key': '2_06', 'anchor': 'C',
 'tab_title': '채굴 경주', 'meta_title': '채굴 — 블록을 쓰는 권리와 그 비용',
 'description': '논스를 바꿔 가며 직접 SHA-256 채굴을 해 보고, 계산력에 따라 블록을 쓸 권리와 보상이 어떻게 나뉘는지 경주로 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인과 비트코인」 p.27–30; Nakamoto (2008) 4·6절',
 'h1': '채굴<br>— 블록을 쓰는 권리와 그 비용', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '다음 블록은 누가 쓰고, 그 비용은 누가 낼까? 위조 사슬을 다시 쓰는 일은 어떻게 비싸질까?',
 'lead': '2-03에서 "다시 쓰기가 너무 싸다"는 문제가 남았습니다. 1-07에서는 "한 표를 무엇으로 정할까"가 남았고요. 비트코인은 둘을 한 번에 풉니다. 블록을 쓰려면 논스를 바꿔 가며 해시가 목표보다 작아질 때까지 계산해야 하고(채굴), 가장 먼저 푼 노드가 블록을 쓰고 보상을 받습니다. 직접 채굴해 보고, 채굴자들의 경주도 돌려 봅니다.',
 'kpis': [('논스', '해시가 목표보다 작아질 때까지 바꾸는 값', 'a', [1]), ('가장 먼저 푼 노드', '새 블록을 만들 권한', 'g', [1]), ('해시 1번', '찾은 답을 확인하는 데 드는 계산 (백서)', 'm', [2]), ('채굴자', '비트코인에서 기록 비용을 내는 쪽', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '블록 쓰기를 비싸게 만들면, 위조자는 그 비싼 일을 뒤 블록마다 다시 해야 해요. 그 "비싼 일"이 채굴이에요.'),
          ('asst', 'smile', 'asst_e13', '여기서 하는 채굴은 진짜 SHA-256 계산이에요. 시도 횟수와 경주 결과를 제가 세어 둘게요.'),
          ('fly', 'point', 'fly_e08', '아무 의미 없는 숫자를 수천 번 돌리는 게 보안이라고? 정말?'),
          ('robo', 'coin', 'robo_e16', '장비 많은 쪽이 이기는 경주라면 내 전문이지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '채굴하고 블록 수를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 장비 한 대로 버틴다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 장비를 늘린다.')],
 'why_title': '왜 채굴인가',
 'why_lead': '채굴은 비트코인과 일반 블록체인 서비스를 가르는 지점이기도 해요. 강의 자료는 둘의 주요 차이를 "분산원장 기록 비용을 누가 내나"로 정리합니다.',
 'why': [('비용을 내는 쪽', '비트코인에서는 채굴자들이 새 블록 생성과 검증의 대가로 비트코인을 받아 참여자들이 자발적으로 비용을 부담한다. 이력관리 서비스에서는 주로 서비스 제공자나 참여 기업이 비용을 부담한다. <sup>[1]</sup>'),
         ('논스와 목표', '채굴은 임의의 논스 값을 대입해 얻은 결과가 제시된 목표(타겟)보다 작아질 때까지 반복하는 작업이며, 이 문제의 어려운 정도가 채굴 난이도다. <sup>[1]</sup>'),
         ('찾기는 어렵고 확인은 쉽다', '백서에서 필요한 평균 작업량은 요구하는 0비트 수에 지수적으로 늘고, 확인은 해시 한 번이면 된다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 채굴의 계산은 쓸모 있는 답을 찾는 게 아니라, 블록 쓰기에 값을 매기는 거예요.'),
 'big_lead': '해시 사슬(2-03)에 "쓰기 비용"을 붙이는 칸입니다. 다음 편(2-07)에서 그 비용이 위조를 얼마나 어렵게 만드는지 계산합니다.',
 'ladder': [('①', '작업증명: 논스 찾기', '블록 하나 쓰는 데 평균 16^d번 계산, 확인은 1번', '누가 블록을 쓸지는 경주로 정해야 한다'),
            ('②', '채굴 경주와 보상', '계산력 몫만큼 블록을 쓰고 보상을 받는다 (CPU 한 표)', '장비가 늘면 블록이 너무 빨리 나온다 → 2-07 난이도')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '논스 찾기', 'title': '목표보다 작은 해시를 찾는다 — 작업증명',
   'tags': [('방식: 논스를 0부터 올리며 SHA-256 반복', 'g'), ('장부: 쪽을 넘기려면 풀어야 하는 자물쇠', '')],
   'left': '<p>장부에 새 쪽을 붙이려면 자물쇠 번호를 맞혀야 한다. 번호는 하나씩 돌려 보는 수밖에 없다. 맞힌 번호가 맞는지는 한 번 돌려 보면 안다. 처음 맞힌 사람이 그 쪽을 쓰고 금화를 받는다.</p>',
   'right': '<p>블록에 들어 있는 논스를 하나씩 올리며 블록 해시가 요구하는 수의 0으로 시작할 때까지 계산한다. <sup>[2]</sup> 교안의 표현으로는 결과 값이 제시된 타겟보다 작아질 때까지 무한 반복한다. <sup>[1]</sup> 일단 계산을 마치면, 그 블록을 바꾸려면 그 작업을 다시 해야 한다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 직접 채굴하기 (SHA-256, 논스 0부터)</h3>
    <div class="hashbox" id="m1data">블록 3|A가 B에게 10,000원을 보냈다|논스 0</div>
    <div class="ctrl"><div class="group"><span class="glabel">난이도 (앞자리 0의 개수)</span><input type="range" id="r1d" min="1" max="4" step="1" value="3" aria-label="채굴 난이도"><span class="val" id="v1d">3</span></div>
      <div class="group"><button class="bt primary" id="b1Mine">▶ 채굴 시작</button><button class="bt" id="b1Reset">처음으로</button></div></div>
    <div class="glabel">지금 계산한 해시</div><div class="hashbox" id="m1hash">—</div>
    <h3>행동으로 보기 — 찾는 데 든 계산 vs 확인하는 데 든 계산</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="채굴 시도 횟수와 검증 횟수(1회), 위조 시 다시 해야 할 계산을 로그 눈금 막대로 비교한 그림"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 0 하나에 16배</h4>
    <ol><li>16진수 해시의 첫 자리가 0일 확률은 1/16. 앞자리 0이 d개면 평균 16<sup>d</sup>번 시도해야 한다.</li>
      <li>찾은 답은 해시 한 번으로 확인한다. 찾기와 확인의 비용이 크게 다르다.</li>
      <li>2-03의 위조자는 이제 고친 블록과 그 뒤 블록을 모두 다시 채굴해야 한다. 다시 쓰기가 더는 공짜가 아니다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 여러 노드가 동시에 채굴하면 누가 블록을 쓰나? 그리고 이 비싼 일을 왜 하나? → 경주와 보상.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>해시 출력이 고르게 퍼져 있다고 보면, 앞 d자리가 모두 0일 확률은 (1/16)<sup>d</sup>, 성공까지 시도 횟수는 기하분포를 따르고 평균은 16<sup>d</sup>이다. 실제 비트코인은 "앞자리 0의 개수"가 아니라 해시를 큰 수로 보고 목표값보다 작은지 비교한다.</p><p class="lim">이 데모의 블록 구성은 단순화했다. 실제 채굴은 블록 머리글(이전 블록 해시, 거래 요약, 시각, 목표, 논스)을 해시한다.</p></details>',
   'say': ('fly', 'type', 'fly_e09', '천 번 넘게 틀리고 겨우 하나 맞혔어. 근데 맞는지 확인은 한 번이네. 위조범은 이걸 블록마다 다시 해야 하고.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '경주와 보상', 'title': '먼저 푼 쪽이 쓴다 — 채굴 경주와 보상',
   'tags': [('방식: 계산력에 비례해 블록을 먼저 찾음', 'g'), ('장부: 쪽마다 붙는 수고비 금화', '')],
   'left': '<p>자물쇠를 여는 사람이 넷이다. 각자 1초에 돌릴 수 있는 횟수가 다르다. 쪽마다 먼저 연 사람이 그 쪽을 쓰고 금화를 받는다. 오래 지켜보면, 손이 두 배 빠른 사람이 쪽을 대략 두 배 많이 쓴다.</p>',
   'right': '<p>가장 먼저 복잡한 수학 문제를 해결한 노드가 새로운 블록을 생성할 권한을 얻는다. <sup>[1]</sup> 블록의 첫 거래는 블록을 만든 사람이 갖는 새 코인을 만드는 특별한 거래다. <sup>[2]</sup> 백서는 이 방식을 "CPU 하나당 한 표"라고 불렀다(1-07의 답). <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 채굴자 넷의 경주 (블록 100개)</h3>
    <div class="cwrap"><canvas id="c2" aria-label="채굴자 넷의 계산력 몫과 블록 100개 중 각자 만든 블록 수를 비교하는 막대그래프"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">Money-Robo 장비 수</span><input type="range" id="r2r" min="1" max="10" step="1" value="4" aria-label="Money-Robo 장비 수"><span class="val" id="v2r">4</span>대</div>
      <div class="group"><span class="glabel">다른 채굴자 둘의 장비 (각자)</span><input type="range" id="r2o" min="0" max="5" step="1" value="1" aria-label="다른 채굴자 장비 수"><span class="val" id="v2o">1</span>대</div>
      <div class="group"><button class="bt primary" id="b2Run">▶ 블록 100개 경주</button></div></div>
    <h3>행동으로 보기 — 블록마다 먼저 찾은 채굴자에게 금화</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="블록이 하나씩 만들어질 때마다 먼저 찾은 채굴자 앞에 금화가 쌓이는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 계산력이 곧 표</h4>
    <ol><li>블록마다 누가 먼저 찾을지는 운이지만, 오래 보면 각자 만든 블록 비율은 계산력 몫에 가까워진다.</li>
      <li>그래서 위조 사슬로 정직한 사슬을 따라잡으려면 계산력 과반이 필요하다. IP 주소처럼 쉽게 늘릴 수 있는 것이 아니라 장비와 전기가 드는 것이 표가 된다.</li>
      <li>보상(새 코인)은 채굴자가 이 비용을 기꺼이 내게 만드는 장치다. 교안은 적절한 보상 설계가 네트워크의 건전성과 지속가능성에 중요하다고 정리한다. <sup>[1]</sup></li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 장비가 늘어날수록 블록이 점점 빨리 나온다. 블록 간격을 일정하게 유지하려면? → 2-07 난이도 조정.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 기록 비용의 두 모델</h4><p>비트코인은 새 코인과 수수료로 채굴자에게 기록 비용을 돌려준다. 쇠고기·고등어 이력 관리 같은 서비스는 토큰 보상 대신 서비스 제공자나 참여 기업이 비용을 낸다. <sup>[1]</sup> 같은 블록체인이라도 "누가 장부를 쓰고 왜 쓰는가"가 다르면 설계가 달라진다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '블록 100개 경주에서 장비 4대인 Money-Robo가 가장 많이 만들었어요. 계산력 몫과 블록 몫이 거의 같아요.')},
 ],
 'duel': {'title': '장비 1대 vs 4대, 블록 100개 경주',
  'intro': '초파리는 채굴 장비 1대, Money-Robo는 같은 장비 4대로 블록 100개를 두고 경주한다(다른 채굴자 없음). 판정 기준은 <b>각자 만든 블록 수</b>(많을수록 좋음). 시드 206으로 고정, 블록마다 먼저 찾을 확률은 계산력 몫에 비례한다(위 실험과 같은 함수).',
  'fly': ('장비 1대', '장비 수가 다가 아니야. 운도 있잖아.', '계산력 몫 20%'),
  'robo': ('장비 4대', '장비 네 배면 블록도 네 배지!', '계산력 몫 80%'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>블록마다 난수 u를 뽑아 u &lt; 1/(1+4)이면 초파리, 아니면 Money-Robo가 먼저 찾은 것으로 한다(계산력 몫 비례). 시드 206, 100번 반복해 센다. 기대값은 20 대 80이다.</p><p class="lim">실제 경주는 각자 논스를 독립적으로 시도하는 과정이지만, 결과적으로 "먼저 찾을 확률 = 계산력 몫"이 된다는 점을 바로 써서 단순화했다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>남아 있던 질문</th><th>채굴이 준 답</th></tr></thead><tbody>
   <tr><td>다시 쓰기가 너무 싸다 (2-03)</td><td>블록마다 평균 16^d번의 계산이 들고, 고친 블록 뒤를 전부 다시 채굴해야 한다</td></tr>
   <tr><td>한 표를 무엇으로 정할까 (1-07)</td><td>계산력. 블록을 쓸 확률이 계산력 몫에 비례한다 (CPU 하나당 한 표)</td></tr>
   <tr><td>기록 비용은 누가 내나 (2-05)</td><td>비트코인은 채굴자가 내고 새 코인·수수료로 보상받는다</td></tr></tbody></table></div>
   <h3>논스와 해시 <span class="stampnote">교안의 비교표</span></h3>
   <div class="tw"><table class="tb"><thead><tr><th>특성</th><th>논스 (Nonce)</th><th>해시 (Hash)</th></tr></thead><tbody>
   <tr><td>정의</td><td>블록체인에서 쓰는 일회성 숫자로, 매번 새로운 값을 가짐</td><td>임의의 데이터를 고정 길이 문자열로 바꾸는 암호화 함수</td></tr>
   <tr><td>목적</td><td>채굴 과정에서 반복적으로 바뀌며 작업증명의 핵심 요소</td><td>데이터 무결성 검증, 효율적인 저장·검색</td></tr>
   <tr><td>특징</td><td>임의의 값, 매번 새로 생성되어 가변적</td><td>입력 크기와 관계없이 고정 길이 출력, 일방향성</td></tr>
   <tr><td>사용</td><td>작업증명(PoW)에서 새 블록 생성·검증에 활용</td><td>블록의 고유 식별자, 변조 여부 확인</td></tr></tbody></table></div>
   <p class="sub">출처: 교안 p.30의 표를 옮김. <sup>[1]</sup></p>''',
 'summary_say': ('doc', 'front', 'doc_e08', '채굴은 블록 쓰기에 값을 매기고, 그 값을 낸 만큼 표와 보상을 줘요. 다음 편은 그 값을 일정하게 유지하는 난이도와, 몇 블록을 기다려야 안전한지예요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 Money-Robo가 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 채굴은 논스를 바꿔 가며 목표보다 작은 해시를 찾는 일이다. 찾기는 어렵고 확인은 쉽다.<br>· 블록을 먼저 찾을 확률은 계산력 몫에 비례한다. 그것이 비트코인의 "한 표"다.<br>· 보상은 채굴자가 그 비용을 내게 만드는 장치다.'),
           ('robo', 'happy', 'robo_e12', '장비 네 배면 블록도 네 배! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'cry', 'fly_e21', '…운으로는 못 뒤집었어. 인정. 근데 장비가 한쪽에 몰리면 그게 바로 과반 문제잖아.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-07, 2장의 마지막. 난이도 조정과, 송금받은 돈을 몇 블록 뒤에 믿을지 계산해요.')],
 'kg_hint': '채굴, 논스, 목표, 보상, 계산력…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인과 비트코인」 p.27 (비트코인 채굴 흐름도, 기록 비용 부담 주체, 토큰 보상 설계), p.28 (가장 먼저 문제를 푼 노드의 블록 생성 권한), p.29 (논스 대입과 타겟), p.30 (논스와 해시 개념 비교표). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 4절(논스 증가, 0비트 수에 지수적인 작업량, 해시 한 번으로 확인, 다시 하지 않으면 바꿀 수 없음, CPU 하나당 한 표), 6절(블록의 첫 거래로 새 코인 생성). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['채굴 데모의 블록 내용과 난이도 표현(앞자리 0 개수) — 단순화한 모형, 해시는 실제 SHA-256', '채굴자 넷의 장비 수 (예시값), 경주 시드 26', '대결: 장비 1대 대 4대, 블록 100개, 시드 206'],
 'gloss_keys': [('채굴', True), ('논스', True), ('목표값', True), ('작업증명', True), ('채굴 보상', True), ('계산력', True), ('채굴 난이도', False), ('해시', False)],
 'gloss_anchor': {'채굴': '#why', '논스': '#lv1', '목표값': '#lv1', '작업증명': '#lv1', '채굴 보상': '#lv2', '계산력': '#lv2', '채굴 난이도': '#why', '해시': '#lv1'},
 'quiz': {
  'lv1': [{'q': '16진수 해시의 앞자리 0이 2개가 되어야 하는 난이도라면 평균 몇 번 시도해야 하나?', 'o': ['16번', '32번', '256번', '65,536번'], 'a': 2, 'why': '한 자리 1/16, 두 자리 1/256 → 평균 256번.', 'hint': '16 × 16.', 'c': 'lab:method/proof-of-work'},
          {'q': '채굴로 찾은 논스가 맞는지 확인하는 데 드는 계산은?', 'o': ['해시 한 번', '채굴과 같은 횟수', '절반', '확인할 수 없다'], 'a': 0, 'why': '찾은 논스를 넣고 한 번 해시해 보면 끝이에요. 백서 4절.', 'hint': '"확인하는 데 든 계산" 막대.', 'c': 'lab:term/nonce'}],
  'lv2': [{'q': '채굴자 A의 계산력이 B의 3배라면, 오랫동안 A와 B가 만든 블록 수의 비는 대략?', 'o': ['1 : 1', '3 : 1', '9 : 1', '1 : 3'], 'a': 1, 'why': '블록을 먼저 찾을 확률이 계산력 몫에 비례해요.', 'hint': '경주 실험.', 'c': 'lab:metric/hash-rate'},
          {'q': '교안이 정리한 비트코인과 이력관리 서비스의 주요 차이는?', 'o': ['분산원장 기록 비용을 누가 부담하는가', '해시 함수를 쓰는가', '블록이 있는가', '인터넷을 쓰는가'], 'a': 0, 'why': '비트코인은 채굴자가 보상을 받고 비용을 내고, 이력관리 서비스는 서비스 제공자·참여 기업이 내요.', 'hint': '교안 p.27.', 'c': 'lab:concept/block-reward'}]},
 'kgspec': {
  'ladder': ['lab:method/proof-of-work', 'lab:method/mining-race'],
  'about': ['lab:method/proof-of-work', 'lab:concept/mining', 'lab:term/nonce', 'lab:concept/block-reward', 'lab:metric/hash-rate'],
  'nodes': [
   ('lab:method/mining-race', 'Method', '채굴 경주 (먼저 푼 노드가 블록을 씀)', 'mining race', '#lv2', '여러 채굴자가 동시에 논스를 찾고, 가장 먼저 찾은 노드가 블록을 쓰고 보상을 받는 방식.', 4, [(LEC, '교안 p.28')]),
   ('lab:limitation/who-writes', 'Limitation', '누가 블록을 쓰나', 'who writes the block', '#lv1', '여러 노드가 동시에 채굴하면 블록을 쓸 노드를 정하는 규칙이 필요하다.', 3),
   ('lab:limitation/blocks-speed-up', 'Limitation', '장비가 늘면 블록이 빨라짐', 'more hardware speeds up blocks', '#lv2', '계산력이 늘수록 같은 난이도의 블록이 더 빨리 찾아져 블록 간격이 짧아진다.', 4),
   ('lab:metric/expected-attempts', 'Metric', '평균 시도 횟수 16^d', 'expected attempts', '#lv1', '앞자리 0이 d개인 해시를 찾는 데 필요한 평균 시도 수.', 4),
   ('lab:metric/blocks-won', 'Metric', '만든 블록 수', 'blocks won', '#duel', '경주에서 각 채굴자가 먼저 찾아 쓴 블록의 수.', 3),
   ('lab:concept/one-cpu-one-vote', 'Concept', 'CPU 하나당 한 표', 'one CPU one vote', '#lv2', '블록을 쓸 권리, 곧 표를 계산력에 비례해 주는 원리.', 4, [(WP, '4절')]),
   ('lab:analogy/padlock-page', 'Analogy', '쪽을 넘기는 자물쇠 ↔ 작업증명', 'padlock per page ~ proof of work', '#lv1', '번호를 돌려 맞혀야 새 쪽을 붙일 수 있고, 맞았는지는 한 번에 확인한다.', 3),
   ('lab:question/core', 'Question', '다음 블록은 누가 쓰고 그 비용은 누가 낼까?', 'Who writes the next block and who pays?', '#top', None, 3),
   ('lab:question/duel', 'Question', '장비 1대와 4대, 블록 100개 경주의 결과는?', '1 vs 4 machines over 100 blocks', '#duel', None, 3),
  ],
  'edges': [
   ('lab:method/proof-of-work', 'lab:prerequisiteOf', 'lab:method/mining-race', '#lv2'),
   ('lab:method/proof-of-work', 'lab:hasLimitation', 'lab:limitation/who-writes', '#lv1'),
   ('lab:limitation/who-writes', 'lab:addressedBy', 'lab:method/mining-race', '#lv2'),
   ('lab:method/mining-race', 'lab:hasLimitation', 'lab:limitation/blocks-speed-up', '#lv2'),
   ('lab:limitation/blocks-speed-up', 'lab:addressedBy', 'lab:concept/mining-difficulty', '#lv2', 'mid'),
   ('lab:term/nonce', 'lab:partOf', 'lab:method/proof-of-work', '#lv1'),
   ('lab:term/target', 'lab:partOf', 'lab:method/proof-of-work', '#lv1'),
   ('lab:concept/hash-function', 'lab:prerequisiteOf', 'lab:method/proof-of-work', '#lv1'),
   ('lab:concept/mining', 'lab:broader', 'lab:method/proof-of-work', '#why'),
   ('lab:concept/block-reward', 'lab:partOf', 'lab:method/mining-race', '#lv2'),
   ('lab:concept/one-cpu-one-vote', 'lab:partOf', 'lab:method/mining-race', '#lv2'),
   ('lab:metric/hash-rate', 'lab:partOf', 'lab:concept/one-cpu-one-vote', '#lv2'),
   ('lab:method/proof-of-work', 'lab:evaluatedBy', 'lab:metric/expected-attempts', '#lv1'),
   ('lab:method/mining-race', 'lab:evaluatedBy', 'lab:metric/blocks-won', '#duel'),
   ('lab:metric/blocks-won', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/who-writes', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:analogy/padlock-page', 'lab:analogyOf', 'lab:method/proof-of-work', '#lv1'),
  ],
  'claims': [
   ('lab:claim/cost-bearer', '비트코인에서는 채굴자가 새 블록 생성·검증의 대가로 비트코인을 받아 기록 비용을 자발적으로 부담하고, 이력관리 서비스에서는 서비스 제공자나 참여 기업이 부담한다', '#why', ['lab:concept/block-reward'], [(LEC, '교안 p.27')], 'F01'),
   ('lab:claim/first-solver', '가장 먼저 복잡한 수학 문제를 해결한 노드가 새로운 블록을 생성할 권한을 얻는다', '#lv2', ['lab:method/mining-race'], [(LEC, '교안 p.28')], 'F02'),
   ('lab:claim/nonce-target', '채굴은 임의의 논스를 대입해 얻은 결과가 제시된 타겟보다 작을 때까지 반복하는 작업이며, 그 어려운 정도가 난이도다', '#why', ['lab:term/nonce', 'lab:term/target'], [(LEC, '교안 p.29')], 'F03'),
   ('lab:claim/exponential-work', '필요한 평균 작업량은 요구하는 0비트 수에 지수적으로 늘고, 확인은 해시 한 번으로 한다', '#why', ['lab:method/proof-of-work', 'lab:metric/expected-attempts'], [(WP, '4절')], 'F04'),
   ('lab:claim/redo-work', '작업증명을 마친 블록은 그 작업을 다시 하지 않고는 바꿀 수 없다', '#lv1', ['lab:method/proof-of-work'], [(WP, '4절')], 'F05'),
   ('lab:claim/coinbase', '블록의 첫 거래는 블록을 만든 사람이 갖는 새 코인을 만드는 특별한 거래다', '#lv2', ['lab:concept/block-reward'], [(WP, '6절')], 'F06'),
   ('lab:claim/one-cpu-vote', '작업증명은 본질적으로 CPU 하나당 한 표다', '#lv2', ['lab:concept/one-cpu-one-vote'], [(WP, '4절')], 'F07'),
   ('lab:claim/reward-design', '토큰 보상은 채굴 활동을 장려하고 네트워크 참여를 유도하는 설계이며, 적절한 보상 설계가 네트워크의 건전성과 지속가능성에 중요하다', '#lv2', ['lab:concept/block-reward'], [(LEC, '교안 p.27')], 'F08'),
  ],
  'sims': [('lab:simulation/mine-sha256', '직접 채굴 실험', '#lv1', ['lab:method/proof-of-work']),
           ('lab:simulation/miner-race', '채굴자 넷 경주 실험', '#lv2', ['lab:method/mining-race']),
           ('lab:simulation/duel-1v4', '장비 1대 대 4대 대결', '#duel', ['lab:metric/blocks-won'])],
 },
}
