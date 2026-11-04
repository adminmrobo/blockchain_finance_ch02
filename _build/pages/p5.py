LEC = "lecture2024blockchain"
PAGE = {
 'num': '2-05', 'slug': 'provenance-cases', 'key': '2_05', 'anchor': 'D',
 'tab_title': '이력 관리 사례', 'meta_title': '블록체인 서비스 사례 — 부동산·쇠고기·고등어의 이력',
 'description': '부동산 거래, 쇠고기 이력 관리, 고등어 유통 사례로 블록체인 이력 기록과 즉시 확인을 직접 실험하고, 처음부터 틀린 입력이라는 한계까지 확인하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인 서비스 사례」 p.19–25',
 'h1': '블록체인 서비스 사례<br>— 부동산·쇠고기·고등어의 이력', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '물건이 여러 손을 거쳐 오는 동안의 이력을 블록체인에 남기면, 중간 바꿔치기를 잡을 수 있을까? 잡지 못하는 것은?',
 'lead': '2-04에서 블록체인은 "적지만 중요한 이력"을 담는 그릇이라고 했습니다. 강의 자료는 그런 이력의 예로 부동산 등기, 쇠고기 이력, 고등어 유통을 듭니다. 세 사례의 공통점은 두 가지, 중요 정보의 안전한 기록과 증인·증빙 없는 즉각 확인입니다. 유통 단계를 직접 따라가며 두 가지를 시험하고, 블록체인이 잡지 못하는 경우도 찾아봅니다.',
 'kpis': [('3가지', '교안의 사례: 부동산 · 쇠고기 · 고등어', 'a', [1]), ('출생 → 판매', '쇠고기 이력의 기록 범위', 'g', [1]), ('QR 코드', '소비자가 고등어 이력을 확인하는 방법', 'm', [1]), ('2가지', '사례의 공통점: 안전한 기록 · 즉각 확인', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '마트의 고등어 한 마리가 어디서 잡혀 어떻게 왔는지, 계산대에서 바로 알 수 있다면요?'),
          ('asst', 'smile', 'asst_e13', '유통 다섯 단계를 만들어 놨어요. 중간에 원산지를 바꿔치기해 보고, 처음부터 거짓으로 입력도 해 볼게요.'),
          ('fly', 'point', 'fly_e08', '처음 입력부터 거짓말이면? 블록체인은 그것도 잡아?'),
          ('robo', 'coin', 'robo_e16', '마지막에 라벨만 확인하면 충분하지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '단계를 기록하고 탐지 수를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. 입력 단계의 거짓을 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 마지막 확인에 건다.')],
 'why_title': '왜 이 사례들인가',
 'why_lead': '세 사례는 모두 "물건이나 권리가 여러 손을 거치는 동안, 중간에 누가 바꿔치기할 수 있는" 상황이에요. 이력 장부가 가장 쓸모 있는 자리입니다.',
 'why': [('부동산', '종이로 출력하는 기존 등기는 위조가 쉬워 범죄에 악용됐다. 블록체인을 도입하면 은행 담당자가 종이 서류 대신 데이터 형식의 토지대장을 직접 확인한다. <sup>[1]</sup>'),
         ('쇠고기', '소의 출생부터 도축·가공·유통·판매까지 모든 단계 정보를 실시간으로 블록체인에 기록하고, 단계마다 고유 식별번호와 상세 정보를 저장해 원산지 사기를 막는다. <sup>[1]</sup>'),
         ('고등어', '가공·유통 전 과정 데이터(원산지, 가공 시간, 운송 경로, 가공 방법)를 사물인터넷 등으로 수집해 분산원장에 기록하고, 소비자는 바코드·QR코드로 전체 이력을 확인한다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 블록체인은 "기록된 뒤의 거짓"을 막아요. "기록되기 전의 거짓"은 따로 막아야 해요.'),
 'big_lead': '이력 장부(2-04)가 실제로 쓰이는 자리입니다. 사례의 공통점 두 가지를 두 칸으로 나눠 시험합니다.',
 'ladder': [('①', '단계별 이력 기록', '중간 단계의 바꿔치기가 앞 단계 기록과 어긋나 드러난다', '처음 입력이 거짓이면 그 거짓도 단단히 보존된다'),
            ('②', '증빙 없는 즉각 확인', '권한 있는 사용자가 기록을 바로 조회해 진위를 판단한다', '기록 비용은 누가 내나 → 2-06 채굴')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '단계별 기록', 'title': '단계마다 기록한다 — 안전한 이력',
   'tags': [('방식: 단계마다 블록에 기록, 앞 단계 해시를 이어받음', 'g'), ('현장: 어획·가공·운송·유통·판매', '')],
   'left': '<p>고등어 상자에 붙은 QR 코드를 찍으면 "부산 앞바다 어획 → 가공장 → 냉장 운송 → 도매 → 마트"가 차례로 나온다. 단계마다 담당자가 기록을 남기고, 다음 담당자는 앞 기록을 이어받아 자기 기록을 덧붙인다.</p>',
   'right': '<p>블록체인을 활용한 서비스의 첫 번째 공통점은 중요 정보의 안전한 기록이다. 단계마다 생긴 데이터가 즉시 블록에 추가되어 영구 보존되고, 모든 참여자가 공유해 투명성과 추적 가능성이 높아진다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 유통 다섯 단계</h3>
    <div class="cwrap"><canvas id="c1" aria-label="유통 다섯 단계의 기록이 사슬로 이어진 그림. 바꿔치기한 단계부터 연결이 끊긴다"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">사례</span><button class="bt" data-case="fish" aria-pressed="true">고등어</button><button class="bt" data-case="beef" aria-pressed="false">쇠고기</button><button class="bt" data-case="land" aria-pressed="false">부동산</button></div>
      <div class="group"><button class="bt warn" id="b1Swap" aria-pressed="false">4단계에서 상자·소유자 바꿔치기</button><button class="bt warn" id="b1Lie" aria-pressed="false">1단계부터 거짓 정보 입력</button></div></div>
    <h3>행동으로 보기 — 상자가 단계를 지나며 기록이 쌓인다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="상자가 다섯 단계를 차례로 지나며 각 단계에 기록 블록이 쌓이는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 중간의 거짓과 처음의 거짓</h4>
    <ol><li>4단계에서 상자를 바꿔치기하면, 4단계 기록의 식별번호는 1~3단계에 적힌 번호와 맞지 않는다. 드러난다.</li>
      <li>1단계에서 처음부터 수입산을 국산 번호로 등록하는 식의 거짓 정보를 입력하면, 뒤 단계는 그 거짓을 그대로 이어받는다. 사슬은 정상이다. 드러나지 않는다.</li>
      <li>블록체인이 보장하는 건 "기록된 내용이 그 뒤로 바뀌지 않았다"이지 "기록된 내용이 사실이다"가 아니다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 처음 입력의 진실성은 블록체인 밖(현장 검사, 센서 인증, 책임자 서명)에서 지켜야 한다.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '중간 바꿔치기는 바로 걸렸어. 근데 처음부터 거짓이면 사슬은 멀쩡하다고 나오네.')},
  {'id': 'lv2', 'no': 2, 'small': '응용', 'nav': '즉각 확인', 'title': '증인·증빙 없이 바로 확인한다',
   'tags': [('방식: 권한 있는 사용자가 기록을 직접 조회', 'g'), ('현장: 은행 창구의 토지대장 확인, 계산대의 QR', '')],
   'left': '<p>예전에는 부동산 담보 대출을 하려면 등기부 등본을 떼어 와야 했다. 종이라 위조될 수 있으니 은행은 다시 확인 전화를 돌린다. 블록체인 기록이 있으면 은행 담당자가 데이터 형식의 토지대장을 직접 조회한다.</p>',
   'right': '<p>두 번째 공통점은 기록된 데이터의 즉각적인 확인 가능성이다. 별도의 "증인"이나 "증빙" 과정 없이 실시간으로 확인할 수 있어, 기존의 복잡한 인증 절차가 크게 간소화된다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 하루 확인 요청 처리</h3>
    <div class="cwrap"><canvas id="c2" aria-label="종이 증빙 방식과 블록체인 조회 방식의 확인 시간과 위조 서류 통과 수를 비교하는 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">하루 확인 요청 수</span><input type="range" id="r2n" min="10" max="500" step="10" value="100" aria-label="하루 확인 요청 수"><span class="val" id="v2n">100</span>건</div>
      <div class="group"><span class="glabel">종이 서류 위조 비율(예시값)</span><input type="range" id="r2f" min="0" max="10" step="1" value="2" aria-label="종이 서류 위조 비율"><span class="val" id="v2f">2</span>%</div>
      <div class="group"><span class="glabel">종이 대조로 위조를 잡는 비율(예시값)</span><input type="range" id="r2c" min="0" max="100" step="10" value="70" aria-label="종이 대조 탐지율"><span class="val" id="v2c">70</span>%</div></div>
    <h3>행동으로 보기 — 창구 두 개</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="종이 서류 창구와 블록체인 조회 창구에 손님이 줄을 서서 처리되는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 증빙을 조회로 바꾸면</h4>
    <ol><li>종이 증빙은 떼어 오고, 받아서, 다시 확인하는 데 시간이 든다. 위조 서류 일부는 그래도 통과한다.</li>
      <li>블록체인 조회는 권한 있는 사용자가 기록을 바로 본다. 기록된 뒤에는 바뀌지 않았다는 것이 보장된다.</li>
      <li>단, ①칸의 한계는 그대로다. 처음 기록이 거짓이면 조회 결과도 거짓이다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 누가 이 기록을 저장·유지하는 비용을 내나? 비트코인은 채굴자가, 이력관리 서비스는 서비스 제공자나 참여 기업이 낸다(교안 p.27). → 2-06 채굴.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면 — 입력 단계를 지키는 장치</h4><p>이력 관리 시스템의 약한 고리는 언제나 첫 입력이다. 현장에서는 사물인터넷 센서로 사람 손을 덜 거치게 하거나(고등어 사례의 데이터 수집), 고유 식별번호를 물리적으로 붙이거나(쇠고기 사례), 입력자에게 책임을 지우는 방식으로 보완한다.</p><p class="lim">센서도 고장 나거나 조작될 수 있다. 블록체인은 센서 값이 "그 뒤로 바뀌지 않았음"을 보장할 뿐, 센서가 옳았음을 보장하지 않는다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '하루 100건이면 종이 방식은 위조 서류가 평균 0.6건 통과하고, 조회 방식은 기록된 뒤의 위조가 0건이에요. 처음 입력이 거짓인 건 둘 다 못 잡아요.')},
 ],
 'duel': {'title': '가짜 원산지 고등어 100상자, 몇 상자를 잡나?',
  'intro': '가짜 원산지 고등어 100상자가 섞였다. 그중 60상자는 유통 중간(4단계)에 라벨을 바꿔치기했고, 40상자는 처음 입력(1단계)부터 거짓 원산지가 적혔다(비율은 예시값). 판정 기준은 <b>가짜로 찾아낸 상자 수</b>(많을수록 좋음). 탐지 규칙은 위 실험과 같은 함수다.',
  'fly': ('단계마다 블록체인 기록 + QR 확인', '단계마다 적어야 중간 바꿔치기를 잡지.', '5단계 기록 사슬'),
  'robo': ('판매 단계에서 라벨만 확인', '마지막 라벨만 보면 되지. 기록은 비용이야!', '최종 라벨 1장'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>탐지 함수 detect(상자, 방식): 블록체인 방식은 단계 기록 사이에 원산지가 달라지거나 해시 연결이 어긋나면 탐지. 라벨 방식은 최종 라벨만 보므로 라벨이 그럴듯하면 통과. 중간 바꿔치기 60상자는 블록체인 방식에서만 걸리고, 처음부터 거짓인 40상자는 두 방식 모두 통과한다.</p><p class="lim">현실의 라벨 확인에도 검사관, 유전자 검사 같은 다른 수단이 있을 수 있다. 이 모형은 "기록만으로" 잡는 경우로 좁혔다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>사례</th><th>기록하는 이력</th><th>확인하는 사람</th><th>블록체인이 막는 것</th><th>막지 못하는 것</th></tr></thead><tbody>
   <tr><td>부동산</td><td>토지대장·거래 기록</td><td>은행 담당자</td><td>종이 등기 위조</td><td>처음 등록 정보의 오류</td></tr>
   <tr><td>쇠고기</td><td>출생·사육·도축·가공·유통·판매 (단계별 식별번호)</td><td>유통업자·소비자</td><td>중간 원산지 바꿔치기</td><td>출생 농장 정보를 처음부터 거짓 입력</td></tr>
   <tr><td>고등어</td><td>원산지·가공 시간·운송 경로·가공 방법</td><td>소비자 (QR)</td><td>유통 중 기록 변조</td><td>센서 고장·조작</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>유통 다섯 단계와 사기 비율은 설명용 모형이다. 실제 시스템의 단계 구성은 품목마다 다르다.</li><li>교안의 사례 화면은 방송 보도 영상을 인용한 것이며, 각 시스템의 세부 기술은 이 페이지에서 확인하지 않았다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '단계마다 기록하면 중간의 거짓이 드러나고, 기록은 바로 조회돼요. 첫 입력의 진실만은 사람과 센서의 몫이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'sigh', 'robo_e20'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, 주판봇이 식은땀을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 사례의 공통점은 중요 정보의 안전한 기록과 증빙 없는 즉각 확인이다.<br>· 단계마다 기록하면 중간 바꿔치기가 드러난다.<br>· 처음부터 거짓으로 입력된 정보는 블록체인도 그대로 지킨다.'),
           ('fly', 'arms', 'fly_e16', '60상자는 잡았어. 40상자는 못 잡았고. 그건 솔직히 말해야지.'),
           ('robo', 'sigh', 'robo_e20', '라벨만 봐서는 한 상자도 못 잡았네… 이번 판은 손절.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-06, 이 기록을 누가 비용을 내고 만드는지, 비트코인의 채굴을 봐요.')],
 'kg_hint': '이력 관리, 원산지, QR, 입력…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인 서비스 사례」 p.19–20 (부동산 거래, 교안이 인용한 보도: "종이 서류 없앤다…부동산 거래에 블록체인"), p.21–22 (쇠고기 이력 관리, 교안이 인용한 보도: "쇠고기 이력 관리에 블록체인 도입"), p.23–24 (고등어 유통, 교안이 인용한 보도: MBC 2022.12.23), p.25 (사례의 공통점). PDF 2024-10-18 생성.'],
 'examples': ['유통 다섯 단계 구성 (설명용 모형)', '하루 확인 요청 100건, 종이 위조 2%, 종이 대조 탐지 70% (예시값)', '대결: 가짜 100상자 중 중간 바꿔치기 60, 처음부터 거짓 40 (예시값)'],
 'gloss_keys': [('이력 관리', True), ('이력', True), ('해시', False), ('분산원장', True), ('무결성', False), ('블록', True)],
 'gloss_anchor': {'이력 관리': '#lv1', '이력': '#lv1', '해시': '#lv1', '분산원장': '#why', '무결성': '#summary', '블록': '#lv1'},
 'quiz': {
  'lv1': [{'q': '유통 4단계에서 원산지를 바꿔치기하면 블록체인 이력에서 어떻게 되나?', 'o': ['앞 단계 기록과 원산지가 맞지 않고 연결이 어긋나 드러난다', '아무 흔적도 남지 않는다', '1단계 기록이 자동으로 바뀐다', '이력이 지워진다'], 'a': 0, 'why': '앞 단계 기록은 그대로라 바꾼 단계와 어긋나요.', 'hint': '"4단계에서 상자·소유자 바꿔치기" 버튼.', 'c': 'lab:method/stage-records'},
          {'q': '블록체인 이력 관리가 막지 못하는 경우는?', 'o': ['처음 입력부터 거짓 정보가 기록된 경우', '중간 단계에서 기록을 고친 경우', '기록을 지운 경우', '기록 순서를 바꾼 경우'], 'a': 0, 'why': '블록체인은 기록된 뒤 바뀌지 않았음을 보장할 뿐, 기록 내용이 사실임을 보장하지 않아요.', 'hint': '"1단계부터 거짓" 버튼.', 'c': 'lab:limitation/garbage-in'}],
  'lv2': [{'q': '하루 확인 요청 100건, 종이 서류 위조 2%, 종이 대조 탐지율 70%라면 하루에 통과하는 위조 서류는 평균 몇 건인가?', 'o': ['0.6건', '2건', '1.4건', '0건'], 'a': 0, 'why': '100 × 0.02 × (1 − 0.7) = 0.6건.', 'hint': '위조 수 × 놓치는 비율.', 'c': 'lab:method/instant-lookup'},
          {'q': '교안이 꼽은 블록체인 서비스의 두 번째 공통점은?', 'o': ['증인·증빙 없이 기록을 즉시 확인할 수 있다', '수수료가 0원이다', '모든 데이터를 무제한 저장한다', '중앙 관리자가 있다'], 'a': 0, 'why': '맞아요. 복잡한 인증 절차가 크게 간소화돼요.', 'hint': '교안 p.25.', 'c': 'lab:method/instant-lookup'}]},
 'kgspec': {
  'ladder': ['lab:method/stage-records', 'lab:method/instant-lookup'],
  'about': ['lab:concept/provenance-tracking', 'lab:method/stage-records', 'lab:method/instant-lookup', 'lab:limitation/garbage-in'],
  'nodes': [
   ('lab:method/stage-records', 'Method', '단계별 이력 기록', 'stage-by-stage records', '#lv1', '유통·거래의 단계마다 기록을 블록에 남기고 다음 단계가 앞 기록을 이어받는 방식.', 3, [(LEC, '교안 p.22, 24')]),
   ('lab:method/instant-lookup', 'Method', '증빙 없는 즉각 확인', 'instant verification without paperwork', '#lv2', '권한 있는 사용자가 별도 증인·증빙 없이 기록을 바로 조회해 진위를 판단하는 것.', 3, [(LEC, '교안 p.25')]),
   ('lab:limitation/garbage-in', 'Limitation', '처음부터 틀린 입력', 'false data at entry', '#lv1', '처음 입력된 정보가 거짓이면 블록체인은 그 거짓도 그대로 보존한다.', 3),
   ('lab:limitation/who-pays', 'Limitation', '기록 비용은 누가 내나', 'who pays for record keeping', '#lv2', '기록을 저장·유지하는 비용을 누가 부담하는지 정해야 한다.', 3, [(LEC, '교안 p.27')]),
   ('lab:concept/case-real-estate', 'Concept', '사례: 부동산 거래', 'case: real estate', '#why', '종이 등기 대신 데이터 형식의 토지대장을 은행이 직접 확인한다.', 2, [(LEC, '교안 p.20')]),
   ('lab:concept/case-beef', 'Concept', '사례: 쇠고기 이력 관리', 'case: beef traceability', '#why', '출생부터 판매까지 단계별 식별번호와 정보를 블록체인에 기록한다.', 2, [(LEC, '교안 p.22')]),
   ('lab:concept/case-mackerel', 'Concept', '사례: 고등어 유통', 'case: mackerel distribution', '#why', '사물인터넷으로 수집한 유통 데이터를 분산원장에 기록하고 QR로 확인한다.', 2, [(LEC, '교안 p.24')]),
   ('lab:metric/caught-fakes', 'Metric', '찾아낸 가짜 상자 수', 'detected fake boxes', '#duel', '가짜 원산지 상자 중 기록으로 찾아낸 수.', 2),
   ('lab:method/final-label-check', 'Method', '판매 단계 라벨만 확인', 'final-label check only', '#duel', '중간 기록 없이 최종 라벨만 보고 판단하는 방식.', 1),
   ('lab:question/core', 'Question', '여러 손을 거치는 동안의 이력을 남기면 바꿔치기를 잡을 수 있을까?', 'Can recording provenance catch substitution?', '#top', None, 2),
   ('lab:question/duel', 'Question', '가짜 원산지 100상자 중 몇 상자를 잡나?', 'How many fake boxes are caught?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:method/stage-records', 'lab:prerequisiteOf', 'lab:method/instant-lookup', '#lv2'),
   ('lab:method/stage-records', 'lab:hasLimitation', 'lab:limitation/garbage-in', '#lv1'),
   ('lab:method/instant-lookup', 'lab:hasLimitation', 'lab:limitation/who-pays', '#lv2'),
   ('lab:limitation/garbage-in', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:method/stage-records', 'lab:partOf', 'lab:concept/provenance-tracking', '#lv1'),
   ('lab:method/instant-lookup', 'lab:partOf', 'lab:concept/provenance-tracking', '#lv2'),
   ('lab:concept/case-real-estate', 'lab:broader', 'lab:concept/provenance-tracking', '#why'),
   ('lab:concept/case-beef', 'lab:broader', 'lab:concept/provenance-tracking', '#why'),
   ('lab:concept/case-mackerel', 'lab:broader', 'lab:concept/provenance-tracking', '#why'),
   ('lab:concept/history-record', 'lab:prerequisiteOf', 'lab:method/stage-records', '#big'),
   ('lab:concept/block', 'lab:partOf', 'lab:method/stage-records', '#lv1'),
   ('lab:method/stage-records', 'lab:contrastsWith', 'lab:method/final-label-check', '#duel'),
   ('lab:method/stage-records', 'lab:evaluatedBy', 'lab:metric/caught-fakes', '#duel'),
   ('lab:method/final-label-check', 'lab:evaluatedBy', 'lab:metric/caught-fakes', '#duel'),
   ('lab:metric/caught-fakes', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:method/distributed-ledger', 'lab:relatedTo', 'lab:concept/case-mackerel', '#why', 'mid'),
   ('lab:concept/hash-function', 'lab:partOf', 'lab:method/stage-records', '#lv1'),
   ('lab:method/stage-records', 'lab:solves', 'lab:concept/integrity', '#lv1'),
  ],
  'claims': [
   ('lab:claim/real-estate', '종이 등기는 위조가 쉬워 범죄에 악용됐고, 블록체인을 쓰면 은행 담당자가 데이터 형식의 토지대장을 직접 확인한다', '#why', ['lab:concept/case-real-estate'], [(LEC, '교안 p.20')], 'F01'),
   ('lab:claim/beef', '쇠고기 이력 시스템은 출생부터 판매까지 모든 단계 정보를 블록체인에 기록하고 단계별 고유 식별번호와 상세 정보를 저장한다', '#why', ['lab:concept/case-beef', 'lab:method/stage-records'], [(LEC, '교안 p.22')], 'F02'),
   ('lab:claim/mackerel', '고등어 유통은 사물인터넷 등으로 원산지·가공 시간·운송 경로·가공 방법을 수집해 분산원장에 기록하고 소비자는 바코드·QR코드로 확인한다', '#why', ['lab:concept/case-mackerel'], [(LEC, '교안 p.24')], 'F03'),
   ('lab:claim/common-1', '블록체인 서비스의 첫 번째 공통점은 중요 정보의 안전한 기록이다', '#lv1', ['lab:method/stage-records'], [(LEC, '교안 p.25')], 'F04'),
   ('lab:claim/common-2', '두 번째 공통점은 별도 증인·증빙 없이 실시간으로 확인할 수 있다는 것이다', '#lv2', ['lab:method/instant-lookup'], [(LEC, '교안 p.25')], 'F05'),
   ('lab:claim/cost-bearer', '비트코인은 채굴자가, 이력관리 서비스는 주로 서비스 제공자나 참여 기업이 기록 비용을 부담한다', '#lv2', ['lab:limitation/who-pays'], [(LEC, '교안 p.27')], 'F06'),
  ],
  'sims': [('lab:simulation/supply-chain', '유통 다섯 단계 실험', '#lv1', ['lab:method/stage-records']),
           ('lab:simulation/two-counters', '창구 두 개 확인 실험', '#lv2', ['lab:method/instant-lookup']),
           ('lab:simulation/duel-fake-boxes', '가짜 상자 대결', '#duel', ['lab:metric/caught-fakes'])],
 },
}
