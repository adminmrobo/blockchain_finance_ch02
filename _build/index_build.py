import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from template import say
from build import CHAPTER, ROOT, SRC
RES = {'2-01': ('R', '주판봇 승'), '2-02': ('F', '초파리 승'), '2-03': ('X', '주판봇 실격'), '2-04': ('R', '주판봇 승'),
       '2-05': ('F', '초파리 승'), '2-06': ('R', '주판봇 승'), '2-07': ('F', '초파리 승')}
COL = {'F': 'var(--c-fly)', 'R': 'var(--c-robo)', 'D': 'var(--amber)', 'X': 'var(--c-fly)'}
DESC = {'2-01': '거래를 블록으로 묶고 머리글에 요약을 담는다. 묶으면 무엇이 줄고 무엇이 늦어지는가.',
        '2-02': '쉼표 하나에 지문이 통째로 바뀌는 해시. 단방향인데도 후보가 적으면 찾히는 이유.',
        '2-03': '이전 블록의 지문을 담아 사슬로 묶는다. 하나를 고치면 뒤가 모두 어긋난다.',
        '2-04': '현재 값만 남기는 데이터베이스와 모든 변경을 남기는 이력. 각자 잘하는 일.',
        '2-05': '고등어·쇠고기·부동산. 단계마다 기록하면 잡히는 것과 끝내 못 잡는 것.',
        '2-06': '논스를 바꿔 가며 직접 SHA-256 채굴. 계산력 몫이 곧 블록을 쓸 권리다.',
        '2-07': '난이도 조정으로 블록 간격을 지키고, 백서의 식으로 기다릴 블록 수를 계산한다.'}
cards = []
for p in CHAPTER['pages']:
    info = json.load(open(os.path.join(SRC, f"info_{p['num']}.json")))
    r, rt = RES[p['num']]
    cards.append(f'<a href="{p["file"]}"><span class="n">{p["num"]}</span> <b>{info["title"]}</b><p>{DESC[p["num"]]}</p>'
                 f'<p class="glabel">대결: {info["duel"]}</p><span class="res" style="color:{COL[r]};border-color:{COL[r]}">{r} · {rt}</span></a>')
tally = {'F': 0, 'R': 0, 'D': 0}
for r, _ in RES.values(): tally['F' if r in 'FX' else r] += 1
html = f'''<!DOCTYPE html><html lang="ko"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>블록체인 2장 블록체인 기술</title>
<meta name="description" content="블록체인 편 2장 「블록체인 기술」 목차: 블록, 해시, 해시 사슬, 이력, 사례, 채굴, 난이도와 확정의 일곱 편">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/lab.css">
</head><body>
<div id="prog" aria-hidden="true"></div>
<nav class="top" aria-label="바로가기"><a class="logo" href="index.html"><i></i>{CHAPTER['short']}</a><a class="l" href="#toc">목차</a><a class="l" href="#ladder">사다리</a><a class="l" href="#score">대결 결산</a><a class="l" href="#about">이 저장소</a></nav>
<header class="hero" id="top"><div class="hex"></div>
  <div class="hero-bg" data-img="bg_ch2_index" role="img" aria-label="금화와 장부가 쌓인 회계실을 픽셀로 그린 배경"><canvas id="heroCv" aria-hidden="true"></canvas></div>
  <div class="wrap"><div class="hero-text">
    <div class="eyebrow">연구실 해설 대시보드 · 블록체인 편</div>
    <h1>2장 블록체인 기술</h1>
    <p class="q">모두가 나눠 든 장부를 어떻게 묶고, 고친 흔적을 어떻게 드러내고, 다시 쓰기를 어떻게 비싸게 만들까?</p>
    <p class="lead">1장은 "모두가 장부를 나눠 든다"에서 끝났습니다. 2장은 그 장부의 부품을 하나씩 엽니다. 블록 → 해시 → 해시 사슬 → 이력 → 사례 → 채굴 → 난이도와 확정. 해시는 모두 브라우저에서 실제 SHA-256으로 계산하고, 마지막 편에서는 백서의 확률 식을 그대로 돌려 봅니다.</p></div>
    <div class="dialog">{say('doc','front','doc_e08','한 편에 두 칸씩, 모두 열네 칸의 사다리예요. 2-01부터 순서대로 읽으면 각 칸이 앞 칸의 한계에서 시작해요.')}
    {say('asst','smile','asst_e13','2-03에서 남은 "다시 쓰기가 너무 싸다"는 문제를 2-06의 채굴이 풀고, 2-07에서 그 효과를 확률로 재요.')}</div>
  </div></header>
<section class="level" id="toc"><div class="wrap"><h2>목차</h2><div class="toc">{''.join(cards)}</div></div></section>
<section class="level" id="ladder"><div class="wrap"><h2>한 장으로 보는 사다리</h2>
  <div class="tw"><table class="tb"><thead><tr><th>편</th><th>다루는 것</th><th>지키는 방법</th><th>남는 약점 → 다음 편</th></tr></thead><tbody>
  <tr><td>2-01</td><td>블록 (묶음 단위)</td><td>거래를 묶고 머리글에 요약</td><td>요약이 원문과 같은지 → 해시</td></tr>
  <tr><td>2-02</td><td>해시 (지문)</td><td>한 글자만 바뀌어도 다른 지문</td><td>지문 하나로는 순서·위치를 못 묶음</td></tr>
  <tr><td>2-03</td><td>해시 사슬</td><td>고치면 뒤 블록이 모두 어긋남</td><td>다시 계산하는 비용이 너무 쌈 → 채굴</td></tr>
  <tr><td>2-04</td><td>이력 (DB와 비교)</td><td>모든 변경을 지우지 않고 남김</td><td>읽기가 느리다, 대량 처리는 DB</td></tr>
  <tr><td>2-05</td><td>이력 관리 사례</td><td>단계별 기록으로 중간 바꿔치기 탐지</td><td>처음부터 거짓 입력은 못 잡음</td></tr>
  <tr><td>2-06</td><td>채굴 (작업증명)</td><td>블록마다 계산 비용, 계산력 몫 = 표</td><td>장비가 늘면 블록이 빨라짐</td></tr>
  <tr><td>2-07</td><td>난이도와 확정</td><td>간격 유지, 기다릴수록 공격 확률 감소</td><td>q ≥ 0.5 공격 → 3장</td></tr></tbody></table></div>
</div></section>
<section class="level" id="score"><div class="wrap"><h2>대결 결산</h2>
  <section class="kpis"><div class="kpi" style="border-top-color:var(--c-fly)"><b>{tally['F']}승</b><span>초파리 연구원 (실격승 1번 포함)</span></div><div class="kpi" style="border-top-color:var(--c-robo)"><b>{tally['R']}승</b><span>주판봇</span></div><div class="kpi a"><b>{tally['D']}번</b><span>무승부</span></div></section>
  {say('doc','judge','doc_e10','2장은 4 대 3. 묶음·속도·장비는 주판봇이, "후보가 적으면?"·"다수 사본과 같은가?"·"몇 블록 기다렸나?" 같은 의심은 초파리가 가져갔다.')}
</div></section>
<section class="level" id="about"><div class="wrap"><h2>이 저장소</h2>
  <p class="sub">각 HTML은 assets/ 폴더의 공용 파일(lab.css, lab.js, sprites.js)을 불러옵니다. 저장소를 통째로 올리거나 내려받아 index.html을 열면 됩니다. 편마다 맨 끝의 "온톨로지·서지 꾸러미"에서 지식 그래프와 참고문헌을 ZIP으로 가져갈 수 있습니다.</p>
  <p class="sub">자료: 강의 교안 「4차산업시대의 금융」 블록체인 단원 p.14–30, Nakamoto (2008). 캐릭터 그림: adminmrobo/fruitfly-lab-expressions (ea5da3f). 저자: 안상선.</p>
  <p class="pn">이전: {CHAPTER['prev_chapter']} · 다음: {CHAPTER['next_chapter']}</p>
</div></section>
<footer><div class="wrap"><p>연구실 해설 대시보드 · 블록체인 편 2장 · v1.0 · 2026-10-29</p></div></footer>
<div id="tip"></div><div id="study"><span id="stTxt">읽은 곳 0%</span><button id="stBtn" hidden>밑줄</button></div>
<script src="assets/sprites.js"></script><script src="assets/lab.js"></script>
<script>Cast.fill();heroArt('C');requestAnimationFrame(loop);addEventListener('scroll',function(){{var h=document.documentElement,p=Math.round(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight));$('#prog').style.width=p+'%';$('#stTxt').textContent='읽은 곳 '+p+'%';}},{{passive:true}});</script>
</body></html>'''
open(os.path.join(ROOT, 'index.html'), 'w').write(html)
print('index ok')
