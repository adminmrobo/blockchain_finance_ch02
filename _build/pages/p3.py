LEC, WP = "lecture2024blockchain", "nakamoto2008bitcoin"
PAGE = {
 'num': '2-03', 'slug': 'hash-chain', 'key': '2_03', 'anchor': 'C',
 'tab_title': '해시 사슬', 'meta_title': '해시 사슬 — 고치면 뒤가 전부 어긋난다',
 'description': '블록마다 앞 블록의 해시를 담아 사슬로 잇고, 한 블록을 고쳤을 때 어긋남이 번지는 모습과 다른 사본과의 대조를 직접 실험하는 해설 페이지',
 'dc_source': '강의 교안 「블록체인의 원리」 p.14–15; Nakamoto (2008) 3·4절',
 'h1': '해시 사슬<br>— 고치면 뒤가 전부 어긋난다', 'hero_alt': '금화와 장부가 쌓인 회계실을 픽셀로 그린 배경',
 'question': '블록마다 앞 블록의 지문을 적어 두면, 중간 블록을 몰래 고쳤을 때 정말 들킬까?',
 'lead': '2-01의 "앞 블록 요약"을 2-02의 해시로 바꿉니다. 각 블록은 자기 데이터와 이전 블록의 해시로 새 해시를 만들고, 이렇게 모든 블록이 연결됩니다. 직접 중간 블록을 고쳐 보고, 위조자가 뒤 블록까지 다 고쳐 맞추면 어떻게 되는지, 그때 다른 사람들의 사본이 어떤 역할을 하는지 봅니다.',
 'kpis': [('이전 블록 해시', '각 블록이 담는 앞 블록의 지문', 'a', [1]), ('모든 후속 블록', '한 블록을 바꾸려면 다시 계산할 범위', 'r', [1, 2]), ('64자', '블록이 몇 개든 앞 블록 지문의 길이', 'g', [1]), ('공개', '누구나 공유하고 검증 가능', 'm', [1])],
 'hero': [('doc', 'think', 'doc_e09', '쪽마다 앞 쪽의 지문을 적은 장부. 중간 쪽을 몰래 고치면 어디서 들킬까요?'),
          ('asst', 'smile', 'asst_e13', '블록 여섯 개를 진짜 SHA-256으로 이어 놨어요. 고치는 버튼, 다시 맞추는 버튼, 다른 사본과 대조하는 버튼까지 있어요.'),
          ('fly', 'point', 'fly_e08', '뒤 블록까지 다 고쳐 맞추면 그만 아냐? 해시 계산은 순식간이잖아.'),
          ('robo', 'coin', 'robo_e16', '내가 고친 사슬도 검사는 전부 통과하게 만들 수 있지. 데이터가 그렇게 말하고 있어요!')],
 'cast': [('doc', 'front', 'doc_e08', '해설과 판정.'), ('asst', 'smile', 'asst_e13', '해시를 계산하고 사본을 대조한다.'),
          ('fly', 'clip', 'fly_e10', '의심하는 쪽. "다시 맞추면?"을 묻는다.'), ('robo', 'smile', 'robo_e13', '확신하는 쪽. 오늘은 위조 사슬을 내민다.')],
 'why_title': '왜 해시로 잇나',
 'why_lead': '2-01에서 합계 요약은 둔했고 전체 복사는 길었어요. 해시는 64자로 짧으면서 한 글자 변화에도 달라져, 두 문제를 함께 풉니다.',
 'why': [('자기 데이터 + 앞 블록 해시', '블록체인에서 각 블록은 자신의 데이터와 이전 블록의 해시 값을 포함하여 새로운 해시를 생성하고, 이런 방식으로 모든 블록이 연결된다. <sup>[1]</sup>'),
         ('뒤가 전부 바뀐다', '하나의 블록을 임의로 변경하려면 연결된 모든 후속 블록의 정보도 함께 수정해야 하는데, 이는 사실상 불가능하다. <sup>[1]</sup>'),
         ('백서의 표현', '각 타임스탬프는 이전 타임스탬프를 해시에 포함해 사슬을 이루고 <sup>[2]</sup>, 블록 뒤에 블록이 이어질수록 그 블록을 바꾸는 일에는 뒤 블록을 모두 다시 하는 일이 포함된다. <sup>[2]</sup>')],
 'why_say': ('doc', 'e07', 'doc_e07', '박사의 한 줄: 해시 사슬은 위조를 막지 않아요. 위조를 숨기려면 뒤를 전부 다시 써야 하게 만들 뿐이에요.'),
 'big_lead': '블록(2-01)과 해시(2-02)를 합쳐 사슬을 만듭니다. 이 편이 끝나면 "다시 써도 금방이면 어떡하나"가 남고, 그 답이 채굴(2-06)입니다.',
 'ladder': [('①', '해시 사슬', '중간 블록을 고치면 바로 뒤 블록에서 드러난다', '위조자가 뒤 블록 해시를 모두 다시 계산하면 사슬 혼자서는 모른다'),
            ('②', '다른 사본과 대조', '다시 맞춘 사슬도 다수의 사본과 끝 해시가 달라 걸린다', '공격자가 과반 사본까지 고치면? 다시 쓰기가 너무 싸다 → 2-06 채굴')],
 'rungs': [
  {'id': 'lv1', 'no': 1, 'small': '핵심', 'nav': '사슬', 'title': '앞 블록의 해시를 담는다 — 해시 사슬',
   'tags': [('방식: hₙ = SHA-256(번호 | 거래 | hₙ₋₁)', 'g'), ('장부: 쪽마다 앞 쪽의 지문', '')],
   'left': '<p>장부 쪽마다 맨 아래에 그 쪽의 지문(해시)을 적고, 다음 쪽 맨 위에 그 지문을 옮겨 적는다. 다음 쪽의 지문은 옮겨 적은 앞 쪽 지문까지 포함해서 만든다. 그래서 앞 쪽 한 글자가 바뀌면 그 뒤의 모든 지문이 바뀐다.</p>',
   'right': '<p>블록이 앞 블록 해시를 담아 새 해시를 만들면 모든 블록이 연결된다. <sup>[1]</sup> 앞 블록 지문은 블록이 몇 개든 늘 64자라, 2-01의 "전체 복사"처럼 길어지지 않는다.</p>',
   'panel': '''<h3>직접 해 보기 — 블록 여섯 개 (실제 SHA-256)</h3>
    <div class="chain" id="chain1" aria-live="polite"></div>
    <div class="ctrl"><div class="group"><span class="glabel">고칠 블록</span><input type="range" id="r1b" min="2" max="6" step="1" value="2" aria-label="고칠 블록 번호"><span class="val" id="v1b">2</span>번</div>
      <div class="group"><button class="bt warn" id="b1Tamper" aria-pressed="false">금액 몰래 고치기</button><button class="bt" id="b1Fix">뒤 블록 해시 전부 다시 계산</button><button class="bt" id="b1Reset">처음으로</button></div></div>
    <h3>행동으로 보기 — 빨간 불이 사슬을 타고 번진다</h3>
    <div class="cwrap"><canvas id="c1b" class="wide" aria-label="블록 여섯 개가 사슬로 이어진 그림. 고친 블록부터 연결이 빨갛게 끊긴다"></canvas></div>
    <section class="kpis" id="k1"></section><div class="eq" id="eq1"></div><div class="insight" id="ins1" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 어긋남은 바로 뒤에서 드러난다</h4>
    <ol><li>블록 j의 금액을 고치면 블록 j의 실제 해시가 적힌 해시와 달라진다.</li>
      <li>블록 j+1에는 블록 j의 옛 해시가 "이전 해시"로 적혀 있어 맞지 않는다.</li>
      <li>숨기려면 j+1의 이전 해시를 고쳐야 하고, 그러면 j+1의 해시가 바뀌어 j+2가 어긋난다. 끝까지 이어진다.</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> "뒤 블록 해시 전부 다시 계산"을 누르면 순식간에 사슬이 다시 초록이 된다. 사슬 혼자서는 위조를 숨긴 사슬을 가려내지 못한다.</p>''',
   'extra': '<details class="math"><summary>수식으로 보기</summary><p><b>hₙ = SHA-256( n | 거래ₙ | hₙ₋₁ )</b>. 블록 j를 고치면 hⱼ가 바뀌고, hⱼ는 hⱼ₊₁의 입력이므로 hⱼ₊₁, hⱼ₊₂, … 가 모두 바뀐다. 따라서 마지막 블록의 해시(끝 해시) 하나가 사슬 전체의 지문 역할을 한다.</p><p class="lim">이 데모의 블록 구성(번호|거래|이전 해시)은 단순화했다. 실제 블록 머리글에는 이전 블록 해시, 거래 요약값, 시각, 난이도 목표, 논스가 들어간다.</p></details>',
   'say': ('fly', 'magnify', 'fly_e07', '고치자마자 바로 뒤 블록이 빨개졌어. 근데 다시 계산 버튼 한 번에 전부 초록으로 돌아왔잖아.')},
  {'id': 'lv2', 'no': 2, 'small': '심화', 'nav': '사본 대조', 'title': '다시 맞춘 사슬은 사본과 대조한다',
   'tags': [('방식: 여러 노드의 끝 해시를 비교해 다수를 따른다', 'g'), ('장부: 아홉 명이 든 같은 장부의 마지막 쪽 지문', '')],
   'left': '<p>위조자가 자기 장부의 2쪽을 고치고 뒤쪽 지문을 전부 새로 써서 앞뒤를 맞췄다. 그 장부 혼자 보면 흠잡을 데가 없다. 하지만 다른 여덟 명의 장부와 마지막 쪽 지문을 맞대 보면 혼자 다르다.</p>',
   'right': '<p>블록체인의 정보는 네트워크에 공개되어 참여자 누구나 공유하고 검증할 수 있다. <sup>[1]</sup> 사슬 전체를 비교할 필요 없이 끝 해시 64자만 맞대 보면 된다. 1-07의 "수천 권 중 바뀐 것을 빨리 알아볼 방법"에 대한 답이다.</p>',
   'panel': '''<h3>직접 해 보기 — 아홉 사본의 끝 해시</h3>
    <div class="cwrap"><canvas id="c2" aria-label="노드 아홉 개의 사슬 끝 해시 앞 8자리를 나란히 보여 주고 다수를 표시한 그림"></canvas></div>
    <div class="ctrl"><div class="group"><span class="glabel">위조자가 함께 고친 사본 수</span><input type="range" id="r2k" min="1" max="9" step="1" value="1" aria-label="위조자가 함께 고친 사본 수"><span class="val" id="v2k">1</span>개</div>
      <div class="group"><button class="bt warn" id="b2Rew" aria-pressed="true">위조 사슬(2번 고치고 뒤 전부 재계산)</button></div></div>
    <h3>행동으로 보기 — 끝 해시만 맞대 본다</h3>
    <div class="cwrap"><canvas id="c2b" class="wide" aria-label="아홉 장부의 마지막 쪽 지문이 가운데로 모여 같은 것끼리 묶이는 장면"></canvas></div>
    <section class="kpis" id="k2"></section><div class="eq" id="eq2"></div><div class="insight" id="ins2" aria-live="polite"></div>''',
   'explain': '''<h4>풀이 — 64자로 사슬 전체를 대조한다</h4>
    <ol><li>사슬의 끝 해시는 앞의 모든 블록 내용에 따라 정해진다. 끝 해시가 같으면 사슬 전체가 같다.</li>
      <li>위조자 혼자 사슬을 다시 맞춰도, 다수의 사본과 끝 해시가 달라 받아들여지지 않는다.</li>
      <li>위조자가 과반 사본을 함께 고치면 위조가 다수가 된다(1-07의 과반 문제 그대로).</li></ol>
    <p class="limit"><b>이 칸의 한계:</b> 해시를 다시 계산하는 데 드는 비용이 거의 0이라, 사본을 장악할 수만 있다면 다시 쓰기는 공짜다. 다시 쓰기를 비싸게 만들어야 한다. → 2-06 채굴(작업증명).</p>''',
   'say': ('asst', 'e10', 'asst_e10', '위조 사슬은 자기 검사를 6블록 다 통과했어요. 그래도 아홉 사본 중 끝 해시가 다른 건 그 하나뿐이었어요.')},
 ],
 'duel': {'title': '다시 맞춘 위조 사슬, 받아들여질까?',
  'intro': 'Money-Robo가 2번 블록의 금액을 고치고, 뒤 블록 해시를 전부 다시 계산한 사슬을 내밀었다. 판정은 <b>사슬 내부 검사를 통과한 블록 수</b>(많을수록 좋음)로 하되, 규칙은 "망의 다수 사본과 같은 사슬만 인정한다". 계산은 위 두 실험과 같은 함수다.',
  'fly': ('원본 사슬 그대로', '고친 데가 없으니 검사도 다 통과하지.', '블록 6개, 원본'),
  'robo': ('2번 고치고 뒤 전부 재계산한 사슬', '봐, 내 사슬도 검사 전부 통과야. 그럼 내 거도 진짜지!', '블록 6개, 위조 후 재계산'),
  'math': '<details class="math"><summary>대결 계산 방식</summary><p>검사 함수 check(사슬): 블록마다 적힌 해시 = 실제 해시, 이전 해시 = 앞 블록 해시인지 센다. 두 사슬 모두 6/6. 대조 함수 compare(사슬, 사본들): 끝 해시가 다수 사본(9개 중 8개)과 다르면 규칙 위반으로 처리한다.</p><p class="lim">이 대결의 "다수 사본"은 9개 노드를 가정한 설명용 모형이다.</p></details>'},
 'summary': '''<div class="tw"><table class="tb"><thead><tr><th>위조자가 한 일</th><th>사슬 혼자 검사</th><th>사본 대조 (공격자 사본 1/9)</th><th>사본 대조 (공격자 사본 5/9)</th></tr></thead><tbody>
   <tr><td>중간 블록만 고침</td><td class="g">걸림 (바로 뒤 블록)</td><td class="g">걸림</td><td class="g">걸림 (사슬 검사)</td></tr>
   <tr><td>고치고 뒤 해시 전부 재계산</td><td class="r">통과</td><td class="g">걸림 (끝 해시 다름)</td><td class="r">통과 (위조가 다수)</td></tr></tbody></table></div>
   <div class="explain"><h4>장부 비유의 한계</h4><ul><li>장부의 "지문"은 사람이 손으로 계산할 수 없다. 해시는 컴퓨터로 순식간에 계산되기 때문에 다시 쓰기가 쉽다는 점이 이 편의 핵심 문제다.</li><li>실제 네트워크는 사본 수를 세는 대신 작업증명이 가장 많이 들어간 사슬을 따른다(2-07).</li></ul></div>''',
 'summary_say': ('doc', 'front', 'doc_e08', '사슬은 위조를 드러내고, 사본 대조는 혼자 고친 사슬을 걸러요. 남은 건 "다시 쓰기가 너무 싸다". 그걸 비싸게 만드는 게 채굴이에요.'),
 'stage': [('doc', 'front', 'doc_e08'), ('fly', 'arms', 'fly_e16'), ('robo', 'blush', 'robo_e14'), ('asst', 'e16', 'asst_e16')],
 'outro_alt': '무대 위에서 초파리 연구원이 팔짱을 끼고, Money-Robo가 머쓱하게 볼을 붉히는 장면',
 'outro': [('doc', 'front', 'doc_e08', '오늘의 세 줄.<br>· 블록마다 앞 블록 해시를 담으면, 중간을 고친 흔적이 뒤로 번진다.<br>· 뒤를 전부 다시 계산하면 사슬 혼자서는 모르지만, 다른 사본의 끝 해시와 다르다.<br>· 사본을 장악하면 다시 쓰기는 공짜다. 다시 쓰기를 비싸게 만들어야 한다.'),
           ('fly', 'arms', 'fly_e16', '검사 통과가 진짜라는 뜻은 아니야. 다들 가진 사본과 같아야 진짜지.'),
           ('robo', 'blush', 'robo_e14', '…스스로 맞춘 사슬은 내 장부일 뿐이었네. 다음엔 정정당당하게.'),
           ('asst', 'e16', 'asst_e16', '다음은 2-04, 블록체인이 데이터베이스와 무엇이 다른지, 왜 "이력"을 쌓는지 봐요.')],
 'kg_hint': '사슬, 이전 해시, 끝 해시, 대조…',
 'footer_refs': ['강의 교안 「4차산업시대의 금융 — 블록체인의 원리」 p.14 (블록의 연결 단위: 체인, 후속 블록 수정), p.15 (각 블록이 자신의 데이터와 이전 블록의 해시로 새 해시 생성). PDF 2024-10-18 생성.',
                 'Nakamoto, S. (2008). <i>Bitcoin: A Peer-to-Peer Electronic Cash System.</i> 3절(타임스탬프가 이전 타임스탬프를 포함해 사슬을 이룸), 4절(뒤에 이어진 블록을 모두 다시 해야 함). 대학 강의 자료실 사본으로 본문 확인.'],
 'examples': ['블록 여섯 개의 거래 내용 (설명용)', '노드 아홉 개, 위조자가 고친 사본 수 (설명용 모형)', 'SHA-256 값은 브라우저가 직접 계산한 실제 값'],
 'gloss_keys': [('해시', True), ('블록', True), ('무결성', False), ('노드', True), ('블록체인', True), ('과반', False)],
 'gloss_anchor': {'해시': '#why', '블록': '#why', '무결성': '#summary', '노드': '#lv2', '블록체인': '#why', '과반': '#lv2'},
 'quiz': {
  'lv1': [{'q': '블록 1~6 사슬에서 3번 블록 금액을 고친 직후(다른 것은 그대로) 검사에 걸리는 블록은?', 'o': ['3번만', '3번과 4번', '1번부터 6번까지 전부', '6번만'], 'a': 1, 'why': '3번은 적힌 해시와 실제 해시가 달라지고, 4번은 적어 둔 "이전 해시"가 3번의 실제 해시와 달라요.', 'hint': '고친 블록과 바로 뒤.', 'c': 'lab:method/hash-chain'},
          {'q': '해시 사슬에서 블록이 1,000개로 늘어나면 각 블록에 적는 "이전 해시"의 길이는?', 'o': ['1,000배로 길어진다', '그대로 64자다', '점점 짧아진다', '블록마다 다르다'], 'a': 1, 'why': '해시는 고정 길이라 앞이 얼마나 길든 64자예요. 2-01의 전체 복사와 다른 점이에요.', 'hint': '해시의 첫 번째 성질.', 'c': 'lab:concept/hash-function'}],
  'lv2': [{'q': '위조자가 자기 사본의 뒤 블록 해시를 전부 다시 계산했다. 이 위조를 가려내는 가장 간단한 방법은?', 'o': ['다른 사본들과 끝 해시를 맞대 본다', '사슬을 처음부터 다시 검사한다', '블록 수를 센다', '방법이 없다'], 'a': 0, 'why': '혼자 검사로는 통과하지만, 다수 사본의 끝 해시와 달라요.', 'hint': '아홉 사본 실험.', 'c': 'lab:method/tip-comparison'},
          {'q': '해시 사슬과 사본 대조만으로 막을 수 없는 경우는?', 'o': ['공격자가 과반 사본을 함께 고칠 때', '공격자가 블록 하나만 고칠 때', '공격자가 사본 하나만 고칠 때', '사슬이 아주 길 때'], 'a': 0, 'why': '위조가 다수가 되면 다수결이 위조를 택해요. 다시 쓰기가 공짜이기 때문이에요.', 'hint': '슬라이더를 5 이상으로.', 'c': 'lab:limitation/cheap-rewrite'}]},
 'kgspec': {
  'ladder': ['lab:method/hash-chain', 'lab:method/tip-comparison'],
  'about': ['lab:method/hash-chain', 'lab:method/tip-comparison', 'lab:limitation/cheap-rewrite'],
  'nodes': [
   ('lab:method/hash-chain', 'Method', '해시로 묶은 블록 사슬', 'hash-linked chain of blocks', '#lv1', '각 블록이 이전 블록의 해시를 담아, 한 블록을 고치면 뒤 블록이 모두 어긋나게 만든 구조.', 3, [(LEC, '교안 p.14–15')]),
   ('lab:method/tip-comparison', 'Method', '끝 해시 대조', 'comparing chain tips', '#lv2', '여러 노드가 가진 사슬의 마지막 블록 해시를 비교해 다수와 다른 사슬을 걸러내는 방법.', 3),
   ('lab:limitation/self-consistent-forgery', 'Limitation', '뒤를 전부 다시 맞춘 위조', 'self-consistent rewritten chain', '#lv1', '위조자가 뒤 블록 해시를 모두 다시 계산하면 사슬 혼자 검사해서는 통과한다.', 3),
   ('lab:limitation/cheap-rewrite', 'Limitation', '다시 쓰기가 너무 쌈', 'rewriting is too cheap', '#lv2', '해시 계산 비용이 거의 0이라, 사본을 장악하면 사슬을 공짜로 다시 쓸 수 있다.', 4),
   ('lab:concept/chain-tip', 'Concept', '끝 해시 (사슬의 지문)', 'chain tip hash', '#lv2', '마지막 블록의 해시. 앞의 모든 블록 내용에 따라 정해져 사슬 전체의 지문 역할을 한다.', 3),
   ('lab:metric/passing-blocks', 'Metric', '내부 검사를 통과한 블록 수', 'blocks passing internal check', '#duel', '적힌 해시와 이전 해시가 모두 맞는 블록의 수.', 3),
   ('lab:analogy/page-fingerprint', 'Analogy', '쪽 아래 지문 ↔ 해시 사슬', 'page fingerprint ~ hash chain', '#lv1', '장부 쪽마다 지문을 적고 다음 쪽에 옮겨 적는다.', 2),
   ('lab:question/core', 'Question', '앞 블록 지문을 적어 두면 중간 블록 위조가 정말 들킬까?', 'Does storing the previous hash expose tampering?', '#top', None, 2),
   ('lab:question/duel', 'Question', '다시 맞춘 위조 사슬은 받아들여질까?', 'Is a recomputed forged chain accepted?', '#duel', None, 3),
  ],
  'edges': [
   ('lab:method/hash-chain', 'lab:prerequisiteOf', 'lab:method/tip-comparison', '#lv2'),
   ('lab:method/hash-chain', 'lab:hasLimitation', 'lab:limitation/self-consistent-forgery', '#lv1'),
   ('lab:limitation/self-consistent-forgery', 'lab:addressedBy', 'lab:method/tip-comparison', '#lv2'),
   ('lab:method/tip-comparison', 'lab:hasLimitation', 'lab:limitation/cheap-rewrite', '#lv2'),
   ('lab:concept/hash-function', 'lab:prerequisiteOf', 'lab:method/hash-chain', '#why'),
   ('lab:concept/block', 'lab:partOf', 'lab:method/hash-chain', '#why'),
   ('lab:method/hash-chain', 'lab:partOf', 'lab:concept/blockchain', '#why'),
   ('lab:concept/chain-tip', 'lab:partOf', 'lab:method/tip-comparison', '#lv2'),
   ('lab:term/node', 'lab:partOf', 'lab:method/tip-comparison', '#lv2'),
   ('lab:concept/majority-vote', 'lab:partOf', 'lab:method/tip-comparison', '#lv2'),
   ('lab:method/hash-chain', 'lab:solves', 'lab:concept/integrity', '#lv1'),
   ('lab:method/hash-chain', 'lab:evaluatedBy', 'lab:metric/passing-blocks', '#duel'),
   ('lab:limitation/self-consistent-forgery', 'lab:raises', 'lab:question/duel', '#duel'),
   ('lab:limitation/cheap-rewrite', 'lab:raises', 'lab:question/core', '#lv2'),
   ('lab:analogy/page-fingerprint', 'lab:analogyOf', 'lab:method/hash-chain', '#lv1'),
  ],
  'claims': [
   ('lab:claim/block-hash-prev', '각 블록은 자신의 데이터와 이전 블록의 해시 값을 포함해 새로운 해시를 생성하고, 이 방식으로 모든 블록이 연결된다', '#why', ['lab:method/hash-chain'], [(LEC, '교안 p.15')], 'F01'),
   ('lab:claim/change-all-following', '하나의 블록을 임의로 변경하려면 연결된 모든 후속 블록의 정보도 수정해야 하며 이는 사실상 불가능하다(강의 자료의 표현)', '#why', ['lab:method/hash-chain', 'lab:limitation/self-consistent-forgery'], [(LEC, '교안 p.14')], 'F02'),
   ('lab:claim/public-verifiable', '블록체인 정보는 네트워크에 공개되어 참여자 누구나 공유·검증할 수 있다', '#lv2', ['lab:method/tip-comparison'], [(LEC, '교안 p.14')], 'F03'),
   ('lab:claim/timestamp-chain', '각 타임스탬프는 이전 타임스탬프를 해시에 포함해 사슬을 이룬다', '#why', ['lab:method/hash-chain'], [(WP, '3절')], 'F04'),
   ('lab:claim/redo-later-blocks', '블록 뒤에 블록이 이어질수록 그 블록을 바꾸는 일에는 뒤 블록을 모두 다시 하는 일이 포함된다', '#why', ['lab:limitation/cheap-rewrite'], [(WP, '4절')], 'F05'),
  ],
  'sims': [('lab:simulation/hash-chain-6', '블록 여섯 개 사슬 실험', '#lv1', ['lab:method/hash-chain']),
           ('lab:simulation/tip-compare', '아홉 사본 끝 해시 대조 실험', '#lv2', ['lab:method/tip-comparison']),
           ('lab:simulation/duel-forged-chain', '위조 사슬 대결', '#duel', ['lab:metric/passing-blocks'])],
 },
}
