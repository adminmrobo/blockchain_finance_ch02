LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '2-01', 'slug': 'block-bundle', 'key': '2_01', 'anchor': 'C',
 'tab_title': '블록: 묶음 단위', 'meta_title': '블록 — 거래를 묶어 장부의 한 쪽으로',
 'description': '거래를 하나씩 적지 않고 블록으로 묶어 이어 붙이는 이유를, 블록 크기와 이어 붙이기를 직접 조작하며 배우는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.14; Nakamoto (2008) 3·5·7절',
 'h1': '블록<br>— 거래를 묶어 장부의 한 쪽으로', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '거래를 하나씩 따로 적지 않고 왜 "블록"으로 묶어서, 그 블록들을 이어 붙일까?',
 'lead': '1장의 끝에서 장부를 모두가 나눠 들었습니다. 2장은 그 장부의 생김새를 봅니다. 블록체인은 데이터를 블록이라는 단위로 저장하고, 블록들을 사슬처럼 순서대로 잇습니다. 이 편은 먼저 "묶는다"와 "잇는다" 두 동작만 떼어서 봅니다.',
 'kpis': [('블록', '데이터를 저장하는 단위', 'a', [1]), ('사슬', '블록을 순서대로 잇는 방식', 'g', [1]), ('약 80바이트', '거래 없는 블록 헤더 크기 (백서)', 'm', [2]), ('모든 후속 블록', '한 블록을 고치려면 함께 고쳐야 할 범위', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '장부는 줄 단위가 아니라 쪽 단위로 넘기죠. 블록이 바로 장부의 한 쪽이에요. 왜 쪽으로 묶을까요?'),
          ('asst', 'smile', 'asst_e13', '거래 1,000건을 블록에 담는 실험을 만들었어요. 블록 크기를 바꾸면 쪽 수와 머리글 양이 어떻게 변하는지 세어 볼게요.'),
          ('fly', 'point', 'fly_e08', '한 건씩 따로 적는 게 더 꼼꼼하지 않아? 묶으면 뭐가 좋은데?'),
          ('robo', 'coin', 'robo_e16', '묶음 판매가 원래 이득이야. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '블록과 바이트를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 한 건씩 꼼꼼히를 고집한다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 묶음에 건다.')],
 'why_title': '왜 블록부터 보나',
 'why_lead': '1-07에서 "수천 권의 장부 중 바뀐 것을 빨리 알아볼 방법"이 숙제로 남았어요. 그 답의 첫 부품이 블록입니다.',
 'why': [('블록 단위로 저장', '분산원장을 블록체인이라고 부르는 것은 데이터를 블록이라는 단위로 저장하고 이를 사슬처럼 연결하기 때문이다. <sup>[1]</sup>'),
         ('이전 블록의 정보', '각 블록은 이전 블록의 정보를 포함한다. 그래서 한 블록을 임의로 바꾸려면 연결된 모든 후속 블록도 함께 고쳐야 한다. <sup>[1]</sup>'),
         ('공개와 검증', '이 정보는 네트워크에 공개되어 참여자 누구나 공유하고 검증할 수 있어 투명성을 보장한다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 블록은 "몇 건을 한 번에 확인할까"의 단위고, 사슬은 "어떤 순서로 확인했나"의 기록이에요.'),
 'big_lead': '2장은 1장이 남긴 두 숙제(빠른 변조 탐지, 투표 단위)를 기술로 푸는 장입니다. 첫 편은 묶음(블록)과 연결(사슬)이라는 뼈대를 세웁니다.',
 'ladder': [('①', '블록: 거래 묶음', '여러 거래를 머리글 하나로 함께 기록·확인한다', '묶음끼리 순서가 없다'),
            ('②', '블록 잇기: 이전 블록 정보 담기', '순서가 생기고, 앞 블록을 바꾸면 뒤가 어긋난다', '"이전 블록 정보"를 짧고 위조가 드러나게 적을 방법 → 2-02 해시')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '묶기', 'title': '거래를 블록으로 묶는다',
   'tags': [('방식: 대기 중인 거래를 모아 블록 하나로', 'g'), ('장부: 거래 여러 줄을 담은 한 쪽', '')],
   'left': '<p>장부 한 쪽에는 맨 위에 날짜와 쪽 번호(머리글)를 적고, 그 아래 거래를 여러 줄 적는다. 쪽이 차면 넘긴다. 한 줄마다 새 쪽을 쓰면 머리글만 수북해진다.</p>',
   'right': '<p>백서에서 노드는 새 거래를 모아 블록에 담는다. <sup>[2]</sup> 블록은 거래 목록과 머리글(헤더)로 이루어지고, 거래가 없는 블록 헤더는 약 80바이트다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 거래 1,000건 묶기</h3>
    <div class="cwrap"><canvas id="c1" aria-label="블록 크기에 따라 블록 수와 머리글이 차지하는 바이트를 보여 주는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">블록 하나에 담는 거래 수</span><input type="range" id="r1s" min="1" max="200" step="1" value="100" aria-label="블록 하나에 담는 거래 수"><span class="val" id="v1s">100</span>건</div>
      <div class="group"><span class="glabel">거래 한 건 크기(예시값)</span><input type="range" id="r1t" min="100" max="500" step="50" value="250" aria-label="거래 한 건 크기"><span class="val" id="v1t">250</span>바이트</div></div>
    <h3>행동으로 보기 — 거래가 쪽에 담기고, 차면 봉인된다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="금화 모양 거래가 날아와 장부 쪽에 쌓이고, 쪽이 차면 머리글이 붙어 사슬 끝에 붙는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 머리글은 쪽마다 하나</h4>
    <ol><li>블록 수 = 거래 수 ÷ 블록 크기(올림). 1,000건을 100건씩 담으면 10블록, 1건씩이면 1,000블록.</li>
      <li>머리글(80바이트)은 블록마다 붙는다. 블록이 많을수록 머리글이 차지하는 몫이 커진다.</li>
      <li>머리글 하나로 그 블록의 거래 전부를 한꺼번에 확인할 수 있게 된다(2-02의 해시가 이 일을 한다).</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 블록이 여러 개 생겼지만 서로 아무 관계가 없다. 어느 블록이 먼저인지, 중간 블록이 빠지거나 바뀌었는지 알 수 없다. → 블록을 잇자.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '한 건씩 쪽을 넘기면 머리글이 거래보다 더 커지겠네. 묶는 게 낭비를 줄이긴 하는구나.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '잇기', 'title': '블록을 잇는다 — 이전 블록의 정보 담기',
   'tags': [('방식: 블록마다 앞 블록의 요약을 적는다', 'g'), ('장부: 쪽 맨 위에 앞 쪽의 요약', '')],
   'left': '<p>새 쪽을 시작할 때 맨 위에 "앞 쪽 요약: 거래 3건, 합계 15,000원"이라고 적는다. 누가 앞 쪽을 몰래 고치면, 다음 쪽 맨 위의 요약과 맞지 않게 된다. 그걸 숨기려면 다음 쪽도, 그다음 쪽도 고쳐야 한다.</p>',
   'right': '<p>각 블록은 이전 블록의 정보를 담는다. 그래서 하나의 블록을 임의로 변경하려면 연결된 모든 후속 블록의 정보도 수정해야 한다. <sup>[1]</sup> 백서의 타임스탬프 서버도 각 타임스탬프가 이전 타임스탬프를 포함해 사슬을 이룬다. <sup>[2]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 앞 쪽 요약으로 잇기</h3>
    <div class="cwrap"><canvas id="c2" aria-label="블록 다섯 개가 이어진 그림. 각 블록 위에 앞 블록 요약(합계)이 적혀 있다"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">고칠 블록</span><input type="range" id="r2b" min="1" max="5" step="1" value="2" aria-label="고칠 블록 번호"><span class="val" id="v2b">2</span>번</div>
      <div class="group"><span class="glabel">요약 방식</span><button class="bt" data-sum="sum" aria-pressed="true">합계만 적기</button><button class="bt" data-sum="list" aria-pressed="false">거래 전부 옮겨 적기</button></div>
      <div class="group"><button class="bt warn" id="b2Edit" aria-pressed="false">금액 몰래 고치기</button><button class="bt warn" id="b2Smart" aria-pressed="false">합계가 같게 두 건을 맞바꿔 고치기</button></div></div>
    <h3>행동으로 보기 — 어긋남이 뒤로 번진다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="블록 사이 연결이 고친 블록부터 빨갛게 바뀌는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 무엇을 요약으로 적을까</h4>
    <ol><li>앞 블록 요약을 담으면 순서가 생기고, 앞 블록을 고친 흔적이 뒤 블록에서 드러난다.</li>
      <li>요약이 "합계"처럼 너무 단순하면, 합계가 같게 두 건을 맞바꾸는 위조는 통과한다.</li>
      <li>거래 전부를 옮겨 적으면 위조는 드러나지만, 블록이 쌓일수록 옮겨 적을 양이 끝없이 커진다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 요약은 짧아야 하고(옮겨 적기 X), 내용이 조금만 바뀌어도 달라져야 한다(합계 X). 두 조건을 함께 만족하는 요약이 필요하다. → 2-02 해시.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p>블록 n의 머리글에 요약 s(블록 n−1)을 적는다. 검사는 "s(블록 n−1을 지금 다시 요약한 값) = 블록 n에 적힌 값"이다. 합계 요약 s = Σ금액 은 금액끼리 맞바꾸는 변경에 둔감하다. 전체 복사 s = 블록 내용 그대로 는 민감하지만 길이가 블록 크기와 같다.</p><p class="lim">이 실험의 "요약"은 해시를 소개하려고 만든 장난감이다. 실제 블록은 다음 편의 해시를 쓴다.</p></details>',
   'say': ('asst', 'e10', 'asst_e10', '합계만 적으면 금액을 맞바꾼 위조는 통과했어요. 전부 옮겨 적으면 걸리지만 5번 블록에는 앞 네 블록의 거래가 다 들어가요.')},
 ],
 'duel': {'title': '거래 1,000건, 블록에 몇 건씩 담을까?',
  'intro': '거래 1,000건(한 건 250바이트, 예시값)을 기록한다. 판정 기준은 <b>머리글을 포함한 총 저장량</b>(적을수록 좋음). 머리글은 블록마다 80바이트(백서의 거래 없는 블록 헤더 크기). 계산은 위 실험과 같은 식이다.',
  'fly': ('거래마다 블록 하나', '한 건씩 따로 봉인해야 꼼꼼하지.', '1,000블록'),
  'robo': ('100건씩 묶어 블록 하나', '묶음이 이득이야. 머리글은 적을수록 좋지!', '10블록'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>총 저장량 = 블록 수 × 80 + 거래 수 × 250. 초파리: 1,000 × 80 + 1,000 × 250 = 330,000바이트. 주판봇: 10 × 80 + 1,000 × 250 = 250,800바이트.</p><p class="lim">블록 크기를 무한정 키울 수는 없다. 블록이 크면 전파와 검증에 시간이 걸린다. 이 대결은 머리글 비용만 따졌다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>칸</th><th>배운 것</th><th>남은 질문</th></tr></thead><tbody>
   <tr><td>① 묶기</td><td>블록은 거래 여러 건과 머리글 하나. 묶을수록 머리글 몫이 준다</td><td>블록 사이 순서는?</td></tr>
   <tr><td>② 잇기</td><td>블록마다 앞 블록 요약을 담으면 순서가 생기고 변조가 뒤로 드러난다</td><td>짧으면서 민감한 요약은?</td></tr></tbody></table></div>
   <div class="explain"><h4>장부 비유의 한계</h4><ul><li>장부의 "쪽"은 크기가 정해져 있지만, 블록 크기는 규칙으로 정한다.</li><li>거래 한 건 250바이트는 예시값이다. 실제 크기는 거래 형태에 따라 다르다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '묶고, 잇는다. 이제 이을 때 적을 "요약"만 정하면 돼요. 다음 편, 해시예요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'coffee', 'fly_e13'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 주판봇이 두 팔을 들고, 초파리 연구원이 커피잔을 든 채 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 블록은 거래 여러 건을 머리글 하나로 묶은 장부의 한 쪽이다.<br>· 블록마다 앞 블록의 정보를 담아 잇는다.<br>· 그 정보는 짧고, 내용이 조금만 바뀌어도 달라져야 한다.'),
           ('robo', 'happy', 'robo_e12', '묶음이 이겼지! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'coffee', 'fly_e13', '…한 건씩 봉인은 머리글 낭비였네. 인정. 근데 요약이 허술하면 묶어도 소용없어.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-02, 그 요약을 만드는 도구인 해시를 직접 계산해 봐요.')],
 'kg_hint': '블록, 헤더, 사슬, 요약…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.14 (데이터의 저장 단위: 블록, 블록의 연결 단위: 체인). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 3절(타임스탬프 사슬), 5절(노드가 거래를 블록에 모음), 7절(거래 없는 블록 헤더 약 80바이트). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['거래 한 건 250바이트, 거래 1,000건 (예시값)', '② 블록 다섯 개, 금액·합계 요약 (설명용 장난감)'],
 'gloss_keys': [('블록', True), ('블록 헤더', True), ('타임스탬프', True), ('블록체인', True), ('분산원장', False)],
 'gloss_anchor': {'블록': '#lv1', '블록 헤더': '#lv1', '타임스탬프': '#lv2', '블록체인': '#why', '분산원장': '#why'},
 'quiz': {
  'lv1': [{'q': '거래 1,000건을 블록 하나에 50건씩 담으면 블록은 몇 개인가?', 'o': ['5개', '20개', '50개', '1,000개'], 'a': 1, 'why': '1,000 ÷ 50 = 20블록.', 'hint': '거래 수 ÷ 블록 크기.', 'c': 'lab:concept/block'},
          {'q': '블록을 크게 묶을수록 줄어드는 것은?', 'o': ['거래 자체의 크기', '머리글(헤더)이 차지하는 총량', '거래 수', '네트워크 참여자 수'], 'a': 1, 'why': '머리글은 블록마다 하나라, 블록 수가 줄면 머리글 총량이 줄어요.', 'hint': '블록마다 하나씩 붙는 것.', 'c': 'lab:term/block-header'}],
  'lv2': [{'q': '블록마다 앞 블록의 정보를 담으면, 3번 블록을 몰래 고칠 때 들키지 않으려면?', 'o': ['3번만 고치면 된다', '3번 뒤의 모든 블록도 고쳐야 한다', '1번 블록만 고치면 된다', '고칠 수 없다'], 'a': 1, 'why': '4번에 적힌 3번 요약이 어긋나고, 그걸 고치면 5번이 어긋나요. 끝까지.', 'hint': '교안 p.14.', 'c': 'lab:method/block-linking'},
          {'q': '"합계"를 앞 블록 요약으로 쓰면 놓치는 위조는?', 'o': ['합계가 같게 금액을 맞바꾼 위조', '금액 하나만 늘린 위조', '블록을 통째로 지운 위조', '블록 순서를 바꾼 위조'], 'a': 0, 'why': '합계가 그대로라 요약이 같아요. 요약은 내용이 조금만 바뀌어도 달라져야 해요.', 'hint': '"합계가 같게 두 건을 맞바꿔 고치기" 버튼.', 'c': 'lab:limitation/weak-summary'}]},
 'kgspec': {
  'ladder': ['lab:concept/block', 'lab:method/block-linking'],
  'about': ['lab:concept/block', 'lab:method/block-linking', 'lab:term/block-header'],
  'nodes': [
   ('lab:method/block-linking', 'Method', '블록 잇기 (이전 블록 정보 담기)', 'linking blocks', '#lv2', '각 블록이 이전 블록의 정보를 담아 순서를 만들고, 앞 블록이 바뀌면 뒤가 어긋나게 하는 방법.', 2, [(LEC, '교안 p.14')]),
   ('lab:limitation/unordered-blocks', 'Limitation', '블록 사이에 순서가 없음', 'blocks have no order', '#lv1', '묶기만 하면 어느 블록이 먼저인지, 중간이 빠졌는지 알 수 없다.', 1),
   ('lab:limitation/weak-summary', 'Limitation', '짧으면서 민감한 요약이 필요함', 'need a short yet sensitive summary', '#lv2', '합계 같은 요약은 맞바꾼 위조를 놓치고, 전체 복사는 끝없이 길어진다.', 2),
   ('lab:metric/storage-bytes', 'Metric', '총 저장량 (바이트)', 'total storage bytes', '#duel', '머리글과 거래를 합친 기록의 크기.', 2),
   ('lab:method/one-tx-per-block', 'Method', '거래마다 블록 하나', 'one transaction per block', '#duel', '거래를 묶지 않고 한 건마다 블록을 만드는 방식.', 1),
   ('lab:analogy/ledger-page', 'Analogy', '장부의 한 쪽 ↔ 블록', 'ledger page ~ block', '#lv1', '머리글과 여러 줄의 거래가 적힌 장부 한 쪽.', 1),
   ('lab:question/core', 'Question', '거래를 왜 블록으로 묶어 이어 붙일까?', 'Why bundle transactions into linked blocks?', '#top', None, 1),
   ('lab:question/duel', 'Question', '거래 1,000건을 블록에 몇 건씩 담을까?', 'How many transactions per block?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:concept/block', 'lab:prerequisiteOf', 'lab:method/block-linking', '#lv2'),
   ('lab:concept/block', 'lab:hasLimitation', 'lab:limitation/unordered-blocks', '#lv1'),
   ('lab:limitation/unordered-blocks', 'lab:addressedBy', 'lab:method/block-linking', '#lv2'),
   ('lab:method/block-linking', 'lab:hasLimitation', 'lab:limitation/weak-summary', '#lv2'),
   ('lab:limitation/weak-summary', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:term/block-header', 'lab:partOf', 'lab:concept/block', '#lv1'),
   ('lab:term/timestamp', 'lab:relatedTo', 'lab:method/block-linking', '#lv2', 'mid'),
   ('lab:method/block-linking', 'lab:partOf', 'lab:concept/blockchain', '#why'),
   ('lab:concept/blockchain', 'lab:broader', 'lab:method/distributed-ledger', '#why'),
   ('lab:concept/block', 'lab:contrastsWith', 'lab:method/one-tx-per-block', '#duel'),
   ('lab:concept/block', 'lab:evaluatedBy', 'lab:metric/storage-bytes', '#duel'),
   ('lab:method/one-tx-per-block', 'lab:evaluatedBy', 'lab:metric/storage-bytes', '#duel'),
   ('lab:metric/storage-bytes', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:analogy/ledger-page', 'lab:analogyOf', 'lab:concept/block', '#lv1'),
  ],
  'claims': [
   ('lab:claim/block-unit', '분산원장을 블록체인이라 부르는 것은 데이터를 블록 단위로 저장하고 사슬처럼 연결하기 때문이다', '#why', ['lab:concept/block', 'lab:concept/blockchain'], [(LEC, '교안 p.14')], 'F01'),
   ('lab:claim/change-all-following', '각 블록은 이전 블록의 정보를 포함해, 한 블록을 바꾸려면 연결된 모든 후속 블록도 고쳐야 한다', '#why', ['lab:method/block-linking'], [(LEC, '교안 p.14')], 'F02'),
   ('lab:claim/public-verifiable', '블록체인 정보는 네트워크에 공개되어 참여자 누구나 공유·검증할 수 있다', '#why', ['lab:concept/blockchain'], [(LEC, '교안 p.14')], 'F03'),
   ('lab:claim/nodes-collect', '노드는 새 거래를 모아 블록에 담는다', '#lv1', ['lab:concept/block'], [(WP, '5절')], 'F04'),
   ('lab:claim/header-80', '거래가 없는 블록 헤더는 약 80바이트다', '#lv1', ['lab:term/block-header'], [(WP, '7절')], 'F05'),
   ('lab:claim/timestamp-chain', '각 타임스탬프는 이전 타임스탬프를 해시에 포함해 사슬을 이룬다', '#lv2', ['lab:term/timestamp', 'lab:method/block-linking'], [(WP, '3절')], 'F06'),
  ],
  'sims': [('lab:simulation/block-packing', '거래 묶기 실험', '#lv1', ['lab:concept/block']),
           ('lab:simulation/summary-link', '앞 블록 요약 잇기 실험', '#lv2', ['lab:method/block-linking']),
           ('lab:simulation/duel-block-size', '블록 크기 대결', '#duel', ['lab:metric/storage-bytes'])],
 },
}
