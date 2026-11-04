LEC = "lecture2024blockchain"
PAGE = {
 'num': '2-04', 'slug': 'history-not-database', 'key': '2_04', 'anchor': 'D',
 'tab_title': 'DB가 아닌 이력', 'meta_title': '데이터베이스가 아닌 이력 — 블록체인이 저장하는 것',
 'description': '현재 값을 덮어쓰는 데이터베이스와 변화의 이력을 쌓는 블록체인을 비교하며, 블록체인이 무엇을 잘하고 무엇에 약한지 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인 서비스 사례」 p.17–18',
 'h1': '데이터베이스가 아닌 이력<br>— 블록체인이 저장하는 것', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '블록체인은 큰 데이터베이스일까? 아니라면 무엇을, 왜 저장할까?',
 'lead': '블록체인은 흔히 데이터베이스의 한 형태로 오해받습니다. 데이터베이스는 중앙 시스템에서 대량 데이터를 효율적으로 다루는 데 중점을 두고, 블록체인은 분산 네트워크에서 데이터의 무결성과 투명성을 지키는 데 주력합니다. 그래서 블록체인은 "지금의 값"이 아니라 "바뀌어 온 이력"을 쌓아요. 두 방식을 같은 계좌 세 개로 비교합니다.',
 'kpis': [('이력', '블록체인이 저장하는 핵심', 'g', [1]), ('지문(해시)', '데이터 자체 대신 저장하는 것', 'a', [1]), ('대량·고속', '데이터베이스가 잘하는 일', 'm', [1]), ('소량·중요', '블록체인이 높은 보안을 주는 데이터', 'r', [1])],
 'hero': [('doc', 'think', 'doc_e09', '도서관 전산 목록은 "지금 이 책이 어디 있나"를 알려 줘요. 대출 기록부는 "이 책이 누구 손을 거쳐 왔나"를 알려 주고요. 블록체인은 어느 쪽일까요?'),
          ('asst', 'smile', 'asst_e13', '같은 계좌 세 개를 데이터베이스 방식과 이력 방식으로 각각 굴려 볼게요. 조회할 때 읽은 줄 수를 세어요.'),
          ('fly', 'point', 'fly_e08', '지금 잔액만 있으면 어제 누가 고쳤는지는 어떻게 알아?'),
          ('robo', 'coin', 'robo_e16', '최신 값만 빠르게! 그게 효율이지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '읽은 줄 수와 답한 질문을 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. "누가 언제 바꿨나"를 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 빠른 조회에 건다.')],
 'why_title': '왜 이력인가',
 'why_lead': '2-01~2-03에서 만든 해시 사슬은 "고치면 드러나는" 장부입니다. 그런 장부에는 무엇을 담아야 할까요? 강의 자료의 답은 "이력"입니다.',
 'why': [('오해 바로잡기', '블록체인은 흔히 데이터베이스의 한 형태로 오해받지만 정확하지 않다. 데이터베이스는 중앙에서 대량 데이터를 효율적으로 관리하고, 블록체인은 분산 네트워크에서 무결성과 투명성 보장에 주력한다. <sup>[1]</sup>'),
         ('무엇을 담나', '블록체인의 핵심은 모든 데이터가 아닌 거래나 사건의 "이력"을 안전하게 기록하는 것이며, 데이터 자체보다 데이터의 지문(해시)을 저장한다. <sup>[1]</sup>'),
         ('왜 이력인가', '고성능 중앙 서버가 없어 대량 데이터를 빠르게 처리할 수 없기 때문에 기술적으로 불가피한 선택이다. 모든 변경이 시간 순서로 기록되고 이전 기록과 연결되어 위조·변조를 막는다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 데이터베이스는 "지금"을 빨리 답하고, 블록체인은 "어떻게 여기까지 왔나"를 증명해요.'),
 'big_lead': '해시 사슬(2-03)이라는 장부가 생겼으니, 거기에 무엇을 넣을지 정합니다. 다음 편(2-05)에서 이 "이력 장부"가 실제로 쓰이는 사례를 봅니다.',
 'ladder': [('①', '데이터베이스 (현재 값 덮어쓰기)', '최신 값을 바로 읽는다, 대량 데이터를 빨리 다룬다', '과거와 변경자를 모르고, 관리자가 고쳐도 흔적이 없다'),
            ('②', '이력 장부 (변화를 쌓기)', '모든 변화를 시간 순서로 남기고, 새 거래를 이력으로 검토해 승인한다', '이력이 쌓일수록 무겁다 → 소량의 중요한 데이터에 쓴다 (2-05)')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '데이터베이스', 'title': '지금의 값을 덮어쓴다 — 데이터베이스',
   'tags': [('방식: 계좌마다 잔액 한 칸, 거래 때마다 덮어쓰기', 'g'), ('일상: 도서관 전산 목록의 "현재 위치"', '')],
   'left': '<p>도서관 전산 목록에는 책마다 "지금 위치: 3층 서가" 한 칸이 있다. 누가 빌려 가면 그 칸을 "대출 중"으로 바꾼다. 지금 어디 있는지는 바로 알지만, 지난달 누가 빌렸는지는 그 칸에 남지 않는다.</p>',
   'right': '<p>데이터베이스는 중앙 시스템에서 대량 데이터를 효율적으로 관리하는 데 중점을 둔다. <sup>[1]</sup> 계좌 잔액처럼 "지금의 값"을 한 칸에 두고 거래 때마다 바꾸면 조회가 빠르다. 블록체인이 대신하려는 것은 이 방식 전체가 아니라, "누가 언제 무엇을 바꿨나"를 증명해야 하는 부분이다.</p>',
   'panel': '''<h3>직접 해 보기 — 잔액 표 세 칸</h3>
    <div class="cwrap"><canvas id="c1" aria-label="A, B, C 세 계좌의 잔액 칸과 감사 질문에 답할 수 있는지 표시한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">거래</span><button class="bt" data-tx="0,1,3000">A → B 3,000</button><button class="bt" data-tx="1,2,2000">B → C 2,000</button><button class="bt" data-tx="2,0,1000">C → A 1,000</button></div>
      <div class="group"><button class="bt warn" id="b1Admin">관리자가 C 잔액을 몰래 +5,000</button><button class="bt" id="b1Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 칸은 셋, 지난 값은 사라진다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="거래가 일어날 때마다 잔액 칸의 숫자가 바뀌고 이전 숫자가 지워지는 장면"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 빠르고 작지만, 과거가 없다</h4>
    <ol><li>몇 번 거래해도 저장하는 칸은 3개, 잔액 조회는 칸 하나만 읽으면 된다.</li>
      <li>"어제 C의 잔액은?" "누가 C의 잔액을 바꿨나?" 같은 질문에는 답할 수 없다. 덮어쓴 값은 사라진다.</li>
      <li>관리자가 칸을 직접 고쳐도 흔적이 남지 않는다. 그래서 중앙 관리자를 믿어야 한다(1-06).</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 과거와 변경자를 증명할 수 없고, 관리자의 변경이 보이지 않는다. → 값을 덮어쓰지 말고 변화를 쌓자.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', 'C 잔액이 갑자기 늘었는데, 표만 봐서는 거래인지 관리자 손인지 몰라.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '이력 장부', 'title': '변화를 쌓는다 — 이력 장부와 이력 검토',
   'tags': [('방식: 거래를 시간 순서로 덧붙이고, 잔액은 이력에서 계산', 'g'), ('일상: 도서관 대출 기록부', '')],
   'left': '<p>대출 기록부에는 "3/2 김○○ 대출, 3/9 반납, 3/10 이○○ 대출"처럼 모든 일이 차례로 적힌다. 지난 줄은 지우지 않는다. 지금 위치를 알려면 기록을 끝까지 읽어야 한다.</p>',
   'right': '<p>블록체인은 데이터 변화의 전체 과정을 추적한다. 새 거래가 들어오면 참여자들이 이력을 검토해 위조나 변조 여부를 확인하고 합의한다. 이 방식은 소량의 중요한 데이터에 높은 수준의 보안을 준다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 이력으로 송금 승인하기</h3>
    <div class="cwrap"><canvas id="c2" aria-label="시간 순서로 쌓인 거래 이력 목록과, 이력에서 다시 계산한 잔액"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">송금 요청</span><button class="bt" data-rq="0,1,3000">A → B 3,000</button><button class="bt" data-rq="1,2,8000">B → C 8,000</button><button class="bt" data-rq="2,0,20000">C → A 20,000</button></div>
      <div class="group"><button class="bt warn" id="b2Old">3번째 이력 금액 몰래 고치기</button><button class="bt" id="b2Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 요청이 이력 검토를 통과해야 덧붙는다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="송금 요청이 들어와 이력을 처음부터 훑는 검토를 거쳐 승인 또는 거절되는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 이력은 답하고, 대신 무겁다</h4>
    <ol><li>잔액은 이력을 처음부터 더해 계산한다. 잔액보다 큰 송금 요청은 이력 검토에서 거절된다.</li>
      <li>이력은 해시 사슬로 묶여 있어(2-03), 지난 줄을 몰래 고치면 그 뒤 연결이 어긋나 드러난다.</li>
      <li>대신 거래가 쌓일수록 기록이 늘고, 검토할 줄도 는다. 강의 자료가 블록체인을 "소량의 중요한 데이터"에 맞는다고 한 이유다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 대량 데이터를 빠르게 처리하는 일에는 맞지 않는다. 그래서 블록체인은 "증명이 필요한 이력"만 담는 쪽으로 쓰인다. → 2-05 이력 관리 사례.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면</h4><p>많은 서비스는 둘을 함께 쓴다. 상세 데이터는 기존 데이터베이스에 두고, 그 데이터의 지문(해시)과 변경 이력만 블록체인에 남겨 "바뀌지 않았음"을 증명한다.</p><p class="lim">실제 블록체인 노드는 매번 이력을 처음부터 다시 더하지 않고, 검증하며 계산해 둔 현재 상태(쓰지 않은 거래 출력 목록 등)를 함께 유지한다. 이 실험의 "처음부터 다시 더하기"는 원리를 보이려는 단순화다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', 'B → C 8,000은 이력상 B 잔액이 모자라 거절됐어요. 3번째 줄을 고치자 그 뒤 연결이 전부 어긋났고요.')},
 ],
 'duel': {'title': '거래 1만 건 뒤, 잔액 조회 1,000번',
  'intro': '거래 10,000건이 차례로 쌓이는 동안 10건마다 한 번씩 잔액을 조회한다(모두 1,000번). 판정 기준은 <b>조회에 읽은 줄의 총수</b>(적을수록 좋음). 초파리는 이력을 처음부터 다시 더하고, 주판봇은 데이터베이스의 잔액 칸을 바로 읽는다.',
  'fly': ('이력을 처음부터 다시 더해 계산', '이력에서 계산해야 믿을 수 있지.', '조회마다 지금까지의 이력 전체'),
  'robo': ('데이터베이스 잔액 칸 바로 읽기', '최신 값 한 칸이면 끝이야!', '조회마다 1줄'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>k번째 조회(10k건이 쌓인 뒤)에서 초파리는 10k줄을 읽는다. 모두 합하면 10 × (1 + 2 + … + 1000) = 5,005,000줄. 주판봇은 조회마다 1줄, 모두 1,000줄.</p><p class="lim">실제 노드는 계산해 둔 현재 상태를 함께 유지해 매번 다시 더하지 않는다. 이 대결은 "이력만 저장할 때의 비용"을 극단적으로 보인 것이다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th></th><th>데이터베이스</th><th>블록체인 (이력)</th></tr></thead><tbody>
   <tr><td>저장하는 것</td><td>현재 값</td><td>변화의 이력 + 데이터의 지문</td></tr>
   <tr><td>강점</td><td class="g">대량 데이터를 빠르게</td><td class="g">누가 언제 바꿨나를 증명, 변조가 드러남</td></tr>
   <tr><td>약점</td><td class="r">과거·변경자 없음, 관리자를 믿어야 함</td><td class="r">쌓일수록 무겁고 느림</td></tr>
   <tr><td>잘 맞는 데이터</td><td>많고 자주 바뀌는 데이터</td><td>적지만 중요하고, 위조되면 안 되는 데이터</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>도서관 목록·기록부 비유는 "현재 값 vs 이력"만 보여 준다. 블록체인 이력은 여러 참여자가 함께 갖고 해시로 묶인다는 점이 다르다.</li><li>현대 데이터베이스도 변경 기록(로그)을 남길 수 있다. 차이는 그 기록을 한 관리자가 지우거나 고칠 수 있느냐다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '블록체인은 모든 데이터를 담는 그릇이 아니에요. 증명이 필요한 이력을 담는 그릇이에요. 다음 편에서 그런 이력의 실제 예를 봐요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('robo', 'happy', 'robo_e12'), ('fly', 'cry', 'fly_e21'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 주판봇이 두 팔을 들고, 초파리 연구원이 폭포 눈물을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 데이터베이스는 현재 값을 덮어쓰고, 대량 데이터를 빠르게 다룬다.<br>· 블록체인은 변화의 이력과 지문을 쌓아 누가 언제 바꿨는지 증명한다.<br>· 그래서 블록체인은 적지만 중요한 데이터에 쓴다.'),
           ('robo', 'happy', 'robo_e12', '조회 속도는 내가 압승! 숫자가 말해 줬잖아. 다음에도 여기에 투자.'),
           ('fly', 'cry', 'fly_e21', '…500만 줄 대 천 줄이라니. 인정. 근데 관리자가 몰래 고친 건 네 표가 못 잡았어.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-05, 부동산·쇠고기·고등어처럼 "이력"이 중요한 실제 사례를 봐요.')],
 'kg_hint': '데이터베이스, 이력, 덮어쓰기, 검토…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인 서비스 사례」 p.17 (활용기술: 데이터베이스가 아닌 "이력" 데이터, 도서관 데이터베이스 그림), p.18 (집중관리 방식과 분산원장 방식, 이력 검토를 통한 송금 승인). PDF 2024-10-18 생성.'],
 'examples': ['계좌 세 개, 시작 잔액 10,000원 (예시값)', '관리자 몰래 변경, 3번째 이력 변조 (설명용 장면)', '대결: 거래 10,000건, 조회 1,000번 (예시값)'],
 'gloss_keys': [('데이터베이스', True), ('이력', True), ('무결성', True), ('해시', False), ('분산원장', False)],
 'gloss_anchor': {'데이터베이스': '#lv1', '이력': '#lv2', '무결성': '#why', '해시': '#why', '분산원장': '#lv2'},
 'quiz': {
  'lv1': [{'q': '잔액 칸을 덮어쓰는 데이터베이스에 거래를 100번 하면 저장하는 칸 수는? (계좌 3개)', 'o': ['3칸', '100칸', '103칸', '300칸'], 'a': 0, 'why': '계좌마다 한 칸, 거래가 몇 번이든 덮어써요.', 'hint': 'KPI의 저장 칸.', 'c': 'lab:method/database'},
          {'q': '덮어쓰기 데이터베이스가 답하지 못하는 질문은?', 'o': ['지금 C의 잔액은?', '어제 C의 잔액은 얼마였고 누가 바꿨나?', '계좌가 몇 개인가?', 'A의 이름은?'], 'a': 1, 'why': '덮어쓴 값과 변경자는 남지 않아요.', 'hint': '과거와 변경자.', 'c': 'lab:limitation/no-history'}],
  'lv2': [{'q': '이력 장부에서 B의 잔액이 5,000원인데 B → C 8,000원 요청이 들어오면?', 'o': ['승인된다', '이력 검토에서 거절된다', 'B 잔액이 음수가 된다', 'C 잔액만 늘어난다'], 'a': 1, 'why': '이력으로 계산한 잔액보다 큰 송금은 검토에서 걸러져요.', 'hint': '이력에서 다시 계산한 잔액.', 'c': 'lab:method/history-ledger'},
          {'q': '강의 자료가 블록체인을 "소량의 중요한 데이터"에 맞는다고 한 이유는?', 'o': ['고성능 중앙 서버가 없어 대량 데이터를 빠르게 처리하기 어렵기 때문', '데이터가 많으면 해시를 못 만들어서', '중요하지 않은 데이터는 불법이라서', '블록 크기가 1바이트라서'], 'a': 0, 'why': '맞아요. 이력을 쌓고 모두가 검토하는 대가로 속도와 용량을 내줘요.', 'hint': '교안 p.18.', 'c': 'lab:limitation/history-weight'}]},
 'kgspec': {
  'ladder': ['lab:method/database', 'lab:method/history-ledger'],
  'about': ['lab:method/database', 'lab:method/history-ledger', 'lab:concept/history-record'],
  'nodes': [
   ('lab:method/history-ledger', 'Method', '이력 장부 (변화를 쌓기)', 'append-only history ledger', '#lv2', '거래를 시간 순서로 덧붙이고, 현재 값은 이력에서 계산하며, 새 거래는 이력을 검토해 승인하는 방식.', 3, [(LEC, '교안 p.18')]),
   ('lab:limitation/no-history', 'Limitation', '과거와 변경자를 모름', 'no history or author of changes', '#lv1', '덮어쓴 값은 사라져 과거 값과 누가 바꿨는지 증명할 수 없고, 관리자의 변경에 흔적이 없다.', 2),
   ('lab:limitation/history-weight', 'Limitation', '이력이 쌓일수록 무거움', 'history grows heavy', '#lv2', '거래가 쌓일수록 기록과 검토할 줄이 늘어, 대량 데이터를 빠르게 처리하기 어렵다.', 3, [(LEC, '교안 p.18')]),
   ('lab:method/history-review', 'Method', '이력 검토로 거래 승인', 'approving by reviewing history', '#lv2', '새 거래가 들어오면 참여자들이 이력을 검토해 위조·변조 여부를 확인하고 합의하는 절차.', 3, [(LEC, '교안 p.18')]),
   ('lab:metric/rows-read', 'Metric', '조회에 읽은 줄 수', 'rows read per query', '#duel', '잔액을 알아내려고 읽어야 하는 기록의 줄 수.', 2),
   ('lab:analogy/library', 'Analogy', '도서관 목록 ↔ 데이터베이스, 대출 기록부 ↔ 이력 장부', 'library catalog vs loan log', '#lv1', '현재 위치만 적힌 목록과 모든 대출·반납이 차례로 적힌 기록부.', 1),
   ('lab:question/core', 'Question', '블록체인은 큰 데이터베이스일까? 아니면 무엇을 왜 저장할까?', 'Is a blockchain a big database?', '#top', None, 2),
   ('lab:question/duel', 'Question', '거래 1만 건 뒤 잔액 조회 비용은 어느 쪽이 적을까?', 'Which is cheaper for balance queries?', '#duel', None, 2),
  ],
  'edges': [
   ('lab:method/database', 'lab:prerequisiteOf', 'lab:method/history-ledger', '#lv2'),
   ('lab:method/database', 'lab:hasLimitation', 'lab:limitation/no-history', '#lv1'),
   ('lab:limitation/no-history', 'lab:addressedBy', 'lab:method/history-ledger', '#lv2'),
   ('lab:method/history-ledger', 'lab:hasLimitation', 'lab:limitation/history-weight', '#lv2'),
   ('lab:method/history-review', 'lab:partOf', 'lab:method/history-ledger', '#lv2'),
   ('lab:concept/history-record', 'lab:partOf', 'lab:method/history-ledger', '#lv2'),
   ('lab:method/history-ledger', 'lab:solves', 'lab:concept/integrity', '#why'),
   ('lab:concept/hash-function', 'lab:partOf', 'lab:method/history-ledger', '#why'),
   ('lab:method/history-ledger', 'lab:broader', 'lab:method/distributed-ledger', '#lv2'),
   ('lab:method/database', 'lab:contrastsWith', 'lab:method/history-ledger', '#duel'),
   ('lab:method/database', 'lab:evaluatedBy', 'lab:metric/rows-read', '#duel'),
   ('lab:method/history-ledger', 'lab:evaluatedBy', 'lab:metric/rows-read', '#duel'),
   ('lab:limitation/history-weight', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/no-history', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:analogy/library', 'lab:analogyOf', 'lab:method/database', '#lv1'),
  ],
  'claims': [
   ('lab:claim/not-database', '블록체인은 데이터베이스의 한 형태로 오해받지만, 데이터베이스는 중앙의 대량 데이터 관리에, 블록체인은 분산 네트워크의 무결성·투명성에 주력한다', '#why', ['lab:method/database', 'lab:method/history-ledger'], [(LEC, '교안 p.17')], 'F01'),
   ('lab:claim/stores-history', '블록체인의 핵심은 거래나 사건의 이력을 안전하게 기록하는 것이며 데이터 자체보다 지문(해시)을 저장한다', '#why', ['lab:concept/history-record', 'lab:concept/hash-function'], [(LEC, '교안 p.17')], 'F02'),
   ('lab:claim/history-why', '고성능 중앙 서버가 없어 대량 데이터를 빠르게 처리할 수 없기 때문에 이력 저장은 기술적으로 불가피한 선택이다', '#why', ['lab:limitation/history-weight'], [(LEC, '교안 p.18')], 'F03'),
   ('lab:claim/review-consensus', '새 거래나 데이터가 추가될 때마다 참여자들이 이력을 검토해 위조·변조를 확인하고 합의하며, 소량의 중요한 데이터에 높은 보안을 준다', '#lv2', ['lab:method/history-review'], [(LEC, '교안 p.18')], 'F04'),
  ],
  'sims': [('lab:simulation/overwrite-db', '잔액 덮어쓰기 실험', '#lv1', ['lab:method/database']),
           ('lab:simulation/history-approve', '이력 검토 송금 실험', '#lv2', ['lab:method/history-ledger']),
           ('lab:simulation/duel-queries', '잔액 조회 비용 대결', '#duel', ['lab:metric/rows-read'])],
 },
}
