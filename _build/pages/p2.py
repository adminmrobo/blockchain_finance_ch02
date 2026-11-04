LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '2-02', 'slug': 'hash-fingerprint', 'key': '2_02', 'anchor': 'D',
 'tab_title': '해시: 데이터의 지문', 'meta_title': '해시 — 데이터의 지문',
 'description': '실제 SHA-256을 계산하며 해시의 고정 길이·눈사태 효과·단방향성을 확인하고, 단방향성이 언제 무너지는지까지 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.15, p.17; Nakamoto (2008) 4절',
 'h1': '해시<br>— 데이터의 지문', 'hero_alt': '사무실 책상과 서류, 두 사람이 금화를 주고받는 픽셀 배경',
 'question': '어떤 길이의 데이터든 짧은 지문 하나로 바꿀 수 있을까? 그 지문에서 원문을 되찾을 수는 없을까?',
 'lead': '2-01은 "짧으면서 내용이 조금만 바뀌어도 달라지는 요약"이 필요하다는 데서 끝났습니다. 그 요약이 해시입니다. 이 페이지의 해시는 그림이 아니라 브라우저가 직접 계산한 진짜 SHA-256 값이에요. 쉼표 하나를 붙여 보고, 원문을 거꾸로 찾아내려고도 해 봅니다.',
 'kpis': [('고정 길이', '어떤 데이터든 같은 길이의 문자열로', 'a', [1]), ('단방향', '해시값에서 원본을 역산할 수 없음', 'g', [1]), ('쉼표 하나', '로도 완전히 다른 해시 (교안의 예)', 'r', [1]), ('SHA-256', '백서가 예로 든 해시 함수', 'm', [2])],
 'hero': [('doc', 'think', 'doc_e09', '사람마다 지문이 다르듯, 데이터마다 지문이 있다면? 그 지문만 비교해도 데이터가 바뀌었는지 알 수 있겠죠.'),
          ('asst', 'smile', 'asst_e13', '여기 계산은 전부 진짜 SHA-256이에요. 바뀐 글자 수와 대입 시도 횟수를 제가 셀게요.'),
          ('fly', 'point', 'fly_e08', '지문에서 사람을 못 찾는다고? 후보가 몇 명 안 되면 한 명씩 대 보면 되잖아.'),
          ('robo', 'coin', 'robo_e16', '거꾸로 못 푼다며. 그럼 해시만 공개하면 무조건 안전이지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '해시를 계산하고 시도 횟수를 센다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. "후보가 적으면?"을 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 단방향이면 다 된다고 본다.')],
 'why_title': '왜 해시인가',
 'why_lead': '해시는 블록체인의 거의 모든 부품에 들어갑니다. 블록 잇기(2-03), 이력 저장(2-04), 채굴(2-06). 먼저 해시 하나의 성질을 손으로 익혀 둡니다.',
 'why': [('고정 길이로 바꾸기', '해시는 임의의 길이를 가진 데이터를 고정된 길이의 암호화된 문자열로 변환하는 함수다. 데이터 크기와 관계없이 효율적인 저장과 검증이 가능하다. <sup>[1]</sup>'),
         ('단방향', '해시 함수는 단방향성을 가져, 해시값으로부터 원본 데이터를 역산하는 것은 불가능하다. <sup>[1]</sup>'),
         ('작은 변화, 큰 차이', '입력 데이터가 조금만 바뀌어도 완전히 다른 해시값이 생성되어, 어떤 데이터라도 변조되면 즉시 감지될 수 있다. <sup>[1]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 해시는 데이터를 감추는 자물쇠가 아니라, 데이터가 그대로인지 확인하는 지문이에요.'),
 'big_lead': '2-01의 "짧고 민감한 요약"을 실제 도구로 만듭니다. 다음 편(2-03)에서 이 지문으로 블록을 잇습니다.',
 'ladder': [('①', '고정 길이 지문', '어떤 데이터든 64자, 한 글자만 바뀌어도 대부분이 바뀐다', '지문에서 원문을 되찾을 수 있다면 쓸모가 줄어든다'),
            ('②', '단방향성과 그 조건', '지문에서 원문을 거꾸로 계산할 수 없다', '입력 후보가 적으면 전부 대입해 찾는다 → 블록에 쓸 때는 큰 입력(2-03)')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '기초', 'nav': '지문', 'title': '어떤 데이터든 64자 지문으로',
   'tags': [('방식: SHA-256, 결과는 16진수 64자', 'g'), ('일상: 사람의 지문', '')],
   'left': '<p>사람의 몸집이 크든 작든 지문은 손가락 끝만 한 크기다. 쌍둥이도 지문이 다르다. 지문만 비교해도 같은 사람인지 알 수 있다. 하지만 지문만 보고 그 사람의 얼굴을 그릴 수는 없다.</p><p class="lim">사람 지문은 비슷한 사람끼리 비슷하지 않지만, 해시는 그보다 더 극단적이다. 입력이 거의 같아도 결과는 완전히 다르다.</p>',
   'right': '<p>SHA-256은 어떤 입력이든 256비트, 16진수 64자로 바꾼다. 백서는 작업증명을 설명하며 해시 함수의 예로 SHA-256을 든다. <sup>[2]</sup> 블록체인은 데이터 자체보다 데이터의 "지문" 또는 "해시"를 저장해 무결성을 보장한다. <sup>[1]</sup></p>',
   'panel': '''<h3>직접 해 보기 — 쉼표 하나의 차이</h3>
    <label class="glabel" for="t1">입력</label>
    <input type="text" id="t1" value="A가 B에게 10,000원을 보냈다" aria-label="해시할 입력">
    <div class="ctrl"><div class="group"><button class="bt" id="b1Comma">끝에 쉼표 하나 추가</button><button class="bt" id="b1Long">긴 글 붙이기 (약 2,000자)</button><button class="bt" id="b1Undo">처음 문장으로</button></div></div>
    <div class="glabel">바로 전 해시</div><div class="hashbox" id="h1prev">—</div>
    <div class="glabel">지금 해시 (바뀐 자리 표시)</div><div class="hashbox" id="h1now">—</div>
    <h3>행동으로 보기 — 256비트 중 어디가 바뀌었나</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="256칸 격자에서 바로 전 해시와 다른 비트가 빨갛게 표시되는 그림"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 세 가지 성질</h4>
    <ol><li><b>고정 길이:</b> 한 글자든 2,000자든 결과는 늘 64자다.</li>
      <li><b>눈사태 효과:</b> 쉼표 하나만 붙여도 256비트 중 약 절반(평균 128비트)이 뒤집힌다. 16진수로는 64자 중 평균 60자가 달라진다.</li>
      <li><b>결정적:</b> 같은 입력은 언제 어디서 계산해도 같은 해시가 나온다. 그래서 서로 다른 컴퓨터가 지문을 맞춰 볼 수 있다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 지문이 원문에 대해 무엇을 드러내는지 아직 확인하지 않았다. 거꾸로 되찾을 수 있다면 쓸모가 줄어든다.</p>''',
   'say': ('fly', 'magnify', 'fly_e07', '쉼표 하나에 비트 절반이 뒤집혔어. 이러면 몰래 고치는 건 바로 티 나겠다.')},
  {'id': 'lv2', 'no': 2, 'small': '핵심', 'nav': '단방향', 'title': '거꾸로는 못 간다 — 단, 후보가 많을 때',
   'tags': [('방식: 해시에서 원문 찾기 = 전부 대입해 보기', 'g'), ('일상: 4자리 자물쇠', '')],
   'left': '<p>번호를 모르는 4자리 자물쇠도 0000부터 9999까지 돌려 보면 언젠가 열린다. 만 번이면 끝이다. 자물쇠가 20자리라면 평생 돌려도 못 연다. 자물쇠가 튼튼해서가 아니라 후보가 너무 많아서다.</p>',
   'right': '<p>해시값에서 원본을 직접 계산해 내는 방법은 없다. <sup>[1]</sup> 남은 방법은 후보를 하나씩 해시해 보고 같은 값이 나오는지 비교하는 것뿐이다. 블록과 거래는 입력이 길고 다양해서 이 방법이 통하지 않는다. 짧은 비밀번호는 다르다.</p>',
   'panel': '''<h3>직접 해 보기 — 4자리 비밀번호의 해시를 거꾸로 찾기</h3>
    <div class="hashbox" id="h2target">—</div>
    <div class="ctrl"><div class="group"><span class="glabel">비밀번호 (공격자는 모름)</span><input type="range" id="r2p" min="0" max="9999" step="1" value="4719" aria-label="숨겨 둔 비밀번호"><span class="val" id="v2p">4719</span></div>
      <div class="group"><span class="glabel">덧붙이는 무작위 비밀 문자 수</span><input type="range" id="r2s" min="0" max="16" step="2" value="0" aria-label="덧붙이는 무작위 문자 수"><span class="val" id="v2s">0</span>자</div>
      <div class="group"><button class="bt primary" id="b2Go">▶ 대입 시작</button><button class="bt" id="b2Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 후보를 하나씩 해시해 비교한다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="0000부터 9999까지 후보 격자가 차례로 지워지며 정답을 찾는 장면, 또는 후보가 너무 많아 끝나지 않는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 단방향성의 진짜 뜻</h4>
    <ol><li>4자리 숫자는 후보가 10,000개뿐이라, 이 브라우저로도 1초 안팎에 찾는다.</li>
      <li>공격자가 모르는 무작위 문자(영문 대소문자·숫자 62종)를 2자 덧붙이면 후보가 3,844배, 8자면 약 218조 배로 늘어난다.</li>
      <li>"원본을 역산할 수 없다"는 말은 계산으로 되돌리는 길이 없다는 뜻이다. 후보가 적으면 대입으로 찾을 수 있다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 해시 하나는 데이터 하나를 지킨다. 블록이 여럿일 때 이 지문으로 블록끼리 어떻게 묶을까? → 2-03 해시 사슬.</p>''',
   'extra': '<div class="bridge field"><h4>현장에 옮기면</h4><p>비밀번호를 해시만 해서 저장하면 짧은 비밀번호는 대입 공격에 뚫린다. 실무에서는 계산을 일부러 느리게 만든 비밀번호 전용 해시 함수와 사용자마다 다른 솔트를 함께 쓴다.</p><p class="lim">이 실험의 "무작위 비밀 문자"는 공격자가 모른다고 가정했다. 실무의 솔트는 보통 해시와 함께 저장되며, 미리 계산한 표를 쓰는 공격을 막는 용도다.</p></div>',
   'say': ('asst', 'e10', 'asst_e10', '4자리는 만 번 안에 찾았어요. 비밀 문자 8자를 덧붙이면 같은 속도로 수천 년이 넘게 걸려요.')},
 ],
 'duel': {'title': '해시만 공개하면 안전할까?',
  'intro': '6자리 숫자 비밀번호를 해시해 공개한다. 공격자는 100만 번까지 대입할 수 있다. 판정 기준은 <b>공격자가 원문을 찾을 확률</b>(낮을수록 좋음). 계산은 위 실험과 같은 식: 찾을 확률 = min(1, 시도 횟수 ÷ 후보 수).',
  'fly': ('비밀 무작위 문자 16자를 덧붙여 해시', '후보가 적으면 다 대입돼. 입력을 길게 만들어.', '후보 10⁶ × 62¹⁶'),
  'robo': ('6자리 숫자만 해시해서 공개', '해시는 거꾸로 못 푼다며? 그럼 그대로 공개해도 안전해.', '후보 10⁶'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>주판봇: 후보 10<sup>6</sup>개, 시도 10<sup>6</sup>번 → 찾을 확률 1. 초파리: 후보 10<sup>6</sup> × 62<sup>16</sup> ≈ 4.8 × 10<sup>34</sup>개 → 찾을 확률 약 2 × 10<sup>−29</sup>.</p><p class="lim">덧붙인 문자가 공격자에게 알려지지 않는다는 가정이다. 알려지면 후보는 다시 10<sup>6</sup>개로 줄어든다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>성질</th><th>뜻</th><th>블록체인에서 쓰이는 곳</th></tr></thead><tbody>
   <tr><td>고정 길이</td><td>어떤 데이터든 64자</td><td>블록 머리글에 앞 블록 지문을 짧게 적는다 (2-03)</td></tr>
   <tr><td>눈사태 효과</td><td>한 글자만 바뀌어도 대부분 바뀐다</td><td>변조가 즉시 드러난다 (2-03, 2-04)</td></tr>
   <tr><td>결정적</td><td>같은 입력은 늘 같은 해시</td><td>모든 노드가 같은 지문을 계산해 맞춰 본다</td></tr>
   <tr><td>단방향</td><td>해시에서 원문을 계산해 낼 수 없다</td><td>원하는 해시가 나오는 입력은 대입으로만 찾는다 → 채굴 (2-06)</td></tr></tbody></table></div>
   <div class="explain"><h4>비유의 한계</h4><ul><li>사람 지문은 우연히 비슷할 수 있지만, 해시는 비슷한 입력에도 완전히 다른 값을 낸다.</li><li>서로 다른 두 입력이 같은 해시를 낼 가능성(충돌)은 0은 아니지만, SHA-256에서 일부러 찾아내는 방법은 알려져 있지 않다.</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '지문은 확인용이지 금고가 아니에요. 이제 이 지문으로 블록을 사슬로 묶어 봐요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'sigh', 'robo_e20'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, 주판봇이 식은땀을 흘리며 인정하는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 해시는 어떤 데이터든 64자 지문으로 바꾼다.<br>· 한 글자만 바뀌어도 지문이 완전히 달라진다.<br>· 지문에서 원문은 계산할 수 없지만, 후보가 적으면 대입으로 찾는다.'),
           ('fly', 'arms', 'fly_e16', '단방향은 "계산으로 못 되돌린다"지 "아무도 못 찾는다"가 아니야.'),
           ('robo', 'sigh', 'robo_e20', '거꾸로 못 푼다는 말만 믿었네… 이번 판은 손절.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-03, 이 지문으로 블록을 사슬처럼 묶고 직접 고쳐 봐요.')],
 'kg_hint': '해시, SHA-256, 눈사태, 단방향…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.15 (해시 알고리즘의 역할, 데이터 변경에 따른 해시값 비교), p.17 (데이터의 지문 또는 해시 저장). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 4절(SHA-256 같은 해시 함수). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['SHA-256 값은 브라우저가 직접 계산한 실제 값', '4자리 비밀번호 4719, 무작위 문자 62종 (설명용)', '대결: 6자리 숫자, 시도 100만 번, 덧붙인 문자 16자 (예시값)'],
 'gloss_keys': [('해시', True), ('SHA-256', True), ('눈사태 효과', True), ('단방향', True), ('무결성', True), ('블록', False)],
 'gloss_anchor': {'해시': '#why', 'SHA-256': '#lv1', '눈사태 효과': '#lv1', '단방향': '#lv2', '무결성': '#lv1', '블록': '#big'},
 'quiz': {
  'lv1': [{'q': '2,000자짜리 글의 SHA-256 해시는 16진수로 몇 자인가?', 'o': ['2,000자', '256자', '64자', '32자'], 'a': 2, 'why': '입력 길이와 관계없이 256비트 = 16진수 64자예요.', 'hint': '"긴 글 붙이기" 버튼.', 'c': 'lab:concept/hash-function'},
          {'q': '입력에 쉼표 하나를 더하면 256비트 중 평균 몇 비트가 바뀌나?', 'o': ['1비트', '약 128비트', '256비트 전부', '0비트'], 'a': 1, 'why': '눈사태 효과로 약 절반이 뒤집혀요.', 'hint': '아래 격자의 빨간 칸 수.', 'c': 'lab:concept/avalanche-effect'}],
  'lv2': [{'q': '4자리 숫자 비밀번호의 해시만 알 때 원문을 찾으려면 최대 몇 번 대입하면 되나?', 'o': ['10번', '1,000번', '10,000번', '찾을 수 없다'], 'a': 2, 'why': '0000~9999, 후보 10,000개를 다 해 보면 반드시 찾아요.', 'hint': '후보의 수.', 'c': 'lab:concept/one-wayness'},
          {'q': '"해시는 단방향이다"의 정확한 뜻은?', 'o': ['해시값에서 원문을 계산해 내는 방법이 없다(후보가 적으면 대입으로는 찾을 수 있다)', '누구도 원문을 영원히 알 수 없다', '해시는 한 번만 계산할 수 있다', '해시값은 하나의 방향으로만 읽는다'], 'a': 0, 'why': '맞아요. 계산으로 되돌리는 길이 없을 뿐이에요.', 'hint': '대결 결과.', 'c': 'lab:limitation/small-input-space'}]},
 'kgspec': {
  'ladder': ['lab:concept/hash-function', 'lab:concept/one-wayness'],
  'about': ['lab:concept/hash-function', 'lab:concept/avalanche-effect', 'lab:concept/one-wayness', 'lab:term/sha-256'],
  'nodes': [
   ('lab:limitation/reversible-risk', 'Limitation', '지문에서 원문을 되찾을 위험', 'risk of recovering input', '#lv1', '지문이 원문을 드러낸다면 확인용 지문으로서 쓸모가 줄어든다.', 2),
   ('lab:limitation/small-input-space', 'Limitation', '입력 후보가 적으면 대입으로 찾음', 'small input space allows brute force', '#lv2', '짧은 비밀번호처럼 후보가 적은 입력은 하나씩 해시해 비교하면 원문을 찾는다.', 3),
   ('lab:concept/determinism', 'Concept', '결정성 (같은 입력, 같은 해시)', 'determinism', '#lv1', '같은 입력은 언제 어디서 계산해도 같은 해시가 나와, 서로 다른 컴퓨터가 지문을 맞춰 볼 수 있다.', 2),
   ('lab:concept/collision', 'Concept', '해시 충돌', 'hash collision', '#summary', '서로 다른 입력이 같은 해시를 내는 것. SHA-256에서 일부러 찾는 방법은 알려져 있지 않다.', 3, None, None, 'mid'),
   ('lab:method/brute-force', 'Method', '대입 공격', 'brute-force search', '#lv2', '후보를 하나씩 해시해 목표 해시와 같은지 비교하는 방법.', 2),
   ('lab:metric/recovery-probability', 'Metric', '원문을 찾을 확률', 'probability of recovering the input', '#duel', '정해진 시도 횟수 안에 원문을 찾을 확률 = min(1, 시도 ÷ 후보 수).', 3),
   ('lab:analogy/fingerprint', 'Analogy', '사람의 지문 ↔ 해시', 'fingerprint ~ hash', '#lv1', '몸집과 상관없이 손끝만 한 크기이고, 지문으로 사람을 확인하지만 지문만으로 얼굴을 그릴 수는 없다.', 1),
   ('lab:analogy/padlock', 'Analogy', '4자리 자물쇠 ↔ 짧은 입력의 해시', '4-digit padlock ~ short-input hash', '#lv2', '후보가 만 개뿐이면 돌려 보면 언젠가 열린다.', 2),
   ('lab:question/core', 'Question', '짧은 지문으로 바꾸고, 지문에서 원문을 되찾을 수 없을까?', 'Can any data become a short fingerprint that cannot be reversed?', '#top', None, 1),
   ('lab:question/duel', 'Question', '해시만 공개하면 안전할까?', 'Is publishing only the hash safe?', '#duel', None, 3),
  ],
  'edges': [
   ('lab:concept/hash-function', 'lab:prerequisiteOf', 'lab:concept/one-wayness', '#lv2'),
   ('lab:concept/hash-function', 'lab:hasLimitation', 'lab:limitation/reversible-risk', '#lv1'),
   ('lab:limitation/reversible-risk', 'lab:addressedBy', 'lab:concept/one-wayness', '#lv2'),
   ('lab:concept/one-wayness', 'lab:hasLimitation', 'lab:limitation/small-input-space', '#lv2'),
   ('lab:limitation/small-input-space', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:term/sha-256', 'lab:broader', 'lab:concept/hash-function', '#lv1'),
   ('lab:concept/avalanche-effect', 'lab:partOf', 'lab:concept/hash-function', '#lv1'),
   ('lab:concept/determinism', 'lab:partOf', 'lab:concept/hash-function', '#lv1'),
   ('lab:concept/collision', 'lab:relatedTo', 'lab:concept/hash-function', '#summary', 'mid'),
   ('lab:method/brute-force', 'lab:contrastsWith', 'lab:concept/one-wayness', '#lv2'),
   ('lab:concept/one-wayness', 'lab:evaluatedBy', 'lab:metric/recovery-probability', '#duel'),
   ('lab:method/brute-force', 'lab:evaluatedBy', 'lab:metric/recovery-probability', '#duel'),
   ('lab:concept/hash-function', 'lab:solves', 'lab:concept/integrity', '#lv1'),
   ('lab:analogy/fingerprint', 'lab:analogyOf', 'lab:concept/hash-function', '#lv1'),
   ('lab:analogy/padlock', 'lab:analogyOf', 'lab:limitation/small-input-space', '#lv2'),
   ('lab:limitation/reversible-risk', 'lab:raises', 'lab:question/core', '#lv1'),
   ('lab:concept/block', 'lab:relatedTo', 'lab:concept/hash-function', '#big', 'mid'),
  ],
  'claims': [
   ('lab:claim/hash-fixed-length', '해시는 임의 길이의 데이터를 고정 길이 문자열로 바꾸어, 데이터 크기와 관계없이 효율적인 저장과 검증을 가능하게 한다', '#why', ['lab:concept/hash-function'], [(LEC, '교안 p.15')], 'F01'),
   ('lab:claim/hash-one-way', '해시 함수는 단방향성을 가져 해시값으로부터 원본을 역산할 수 없다', '#why', ['lab:concept/one-wayness'], [(LEC, '교안 p.15')], 'F02'),
   ('lab:claim/hash-avalanche', '입력이 조금만 바뀌어도(쉼표 하나) 완전히 다른 해시값이 생성되어 변조가 즉시 감지된다', '#why', ['lab:concept/avalanche-effect'], [(LEC, '교안 p.15')], 'F03'),
   ('lab:claim/store-fingerprint', '블록체인은 데이터 자체보다 데이터의 지문(해시)을 저장해 무결성을 보장한다', '#lv1', ['lab:concept/integrity', 'lab:concept/hash-function'], [(LEC, '교안 p.17')], 'F04'),
   ('lab:claim/sha256-example', '백서는 작업증명을 설명하며 해시 함수의 예로 SHA-256을 든다', '#lv1', ['lab:term/sha-256'], [(WP, '4절')], 'F05'),
  ],
  'sims': [('lab:simulation/comma-hash', '쉼표 해시 실험', '#lv1', ['lab:concept/avalanche-effect']),
           ('lab:simulation/pin-brute', '4자리 비밀번호 대입 실험', '#lv2', ['lab:concept/one-wayness']),
           ('lab:simulation/duel-hash-publish', '해시 공개 대결', '#duel', ['lab:metric/recovery-probability'])],
 },
}
