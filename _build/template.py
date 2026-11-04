"""Page template for the blockchain chapter series (ai-lab-explainer v1.7)."""
import json, html

NAMES = {'doc': '박사', 'asst': '하루(조수)', 'fly': '초파리 연구원', 'robo': '주판봇'}
ANCHOR_LEFT = {'A': '초파리에서는', 'B': '연구실에서는', 'C': '장부로 보면', 'D': '일상으로 치면'}

def say(who, mood, img, text, cls=''):
    return (f'<div class="say {cls}" data-who="{who}"><img class="who" data-who="{who}" data-mood="{mood}" data-img="{img}" alt="" aria-hidden="true">'
            f'<div><b class="name">{NAMES[who]}</b><p>{text}</p></div></div>')

def js(o):
    return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')

def kpi_html(kp):
    out = []
    for v, label, cls, refs in kp:
        sup = (' <sup>' + ''.join(f'[{r}]' for r in refs) + '</sup>') if refs else ''
        out.append(f'<div class="kpi {cls}"><b>{v}</b><span>{label}{sup}</span></div>')
    return '<section class="kpis" aria-label="숫자 요약">' + ''.join(out) + '</section>'

def rung(r, anchor):
    left = r.get('left_title', ANCHOR_LEFT[anchor])
    tags = ''.join(f'<span class="lvtag {c}">{t}</span>' for t, c in r['tags'])
    return f'''
<section class="level" id="{r['id']}"><div class="wrap">
  <div class="lvhead"><div class="hexno">{r['no']}<small>{r['small']}</small></div><h2>{r['title']}</h2>
    <p class="sub">{tags}</p></div>
  <div class="pair">
    <div><div class="tag fly">{left}</div>{r['left']}</div>
    <div><div class="tag nn">{r.get('right_title','블록체인에서는')}</div>{r['right']}</div>
  </div>
  <section class="panel">{r['panel']}</section>
  <div class="explain">{r['explain']}</div>
  {r.get('extra','')}
  {say(*r['say'])}
  <div class="quiz" data-quiz="{r['id']}"></div>
</div></section>'''

def page(P, chapter, assets='assets/'):
    num = P['num']
    navlinks = ''.join(f'<a class="l" href="#{r["id"]}">{["①","②","③"][i]} {r["nav"]}</a>' for i, r in enumerate(P['rungs']))
    hero_dialog = ''.join(say(*h) for h in P['hero'])
    cast = ''.join(f'<div><img class="who" data-who="{w}" data-mood="{m}" data-img="{k}" alt="" aria-hidden="true"><div><b style="color:var(--c-{w})">{NAMES[w]}</b><small>{d}</small></div></div>'
                   for w, m, k, d in P['cast'])
    steps = ''.join(f'<div><b class="n">{i+1}</b><b>{t}</b><p class="sub" style="margin:.3em 0 0">{d}</p></div>' for i, (t, d) in enumerate(P['why']))
    path = ''.join(
        f'<a class="pchip{" on" if p["num"]==num else ""}" href="{p["file"]}"{" aria-current=\"page\"" if p["num"]==num else ""}><b>{p["num"]}</b> {p["short"]}</a>'
        for p in chapter['pages'])
    ladder_rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class="r">{d}</td></tr>' for a, b, c, d in P['ladder'])
    rungs = ''.join(rung(r, P['anchor']) for r in P['rungs'])
    D = P['duel']
    stage = ''.join(f'<img data-who="{w}" data-mood="{m}" data-img="{k}" alt="" aria-hidden="true">' for w, m, k in P['stage'])
    outro = ''.join(say(*o) for o in P['outro'])
    refs_li = ''.join(f'<li id="ref{i+1}">{t}</li>' for i, t in enumerate(P['footer_refs']))
    ex_li = ''.join(f'<li>{t}</li>' for t in P['examples'])
    idx = [p['num'] for p in chapter['pages']].index(num)
    prev = chapter['pages'][idx-1] if idx > 0 else None
    nxt = chapter['pages'][idx+1] if idx < len(chapter['pages'])-1 else None
    pn = (f'<a href="{prev["file"]}">← {prev["num"]} {prev["short"]}</a>' if prev else chapter.get('prev_chapter', '—'))
    nn = (f'<a href="{nxt["file"]}">{nxt["num"]} {nxt["short"]} →</a>' if nxt else chapter.get('next_chapter', '—'))
    M = P['meta']
    return f'''<!DOCTYPE html><html lang="ko"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{P['tab_title']}</title>
<meta name="description" content="{html.escape(P['description'])}">
<meta name="citation_title" content="{html.escape(M['title'])}"><meta name="citation_author" content="안상선">
<meta name="citation_publication_date" content="2026/10/29"><meta name="citation_language" content="ko">
<meta name="dc.title" content="{html.escape(M['title'])}"><meta name="dc.creator" content="안상선"><meta name="dc.date" content="2026-10-29">
<meta name="dc.language" content="ko"><meta name="dcterms.isPartOf" content="{html.escape(M['series'])}"><meta name="dcterms.source" content="{html.escape(P['dc_source'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}lab.css">
</head><body>
<div id="prog" aria-hidden="true"></div>
<nav class="top" aria-label="섹션 바로가기">
  <a class="logo" href="index.html"><i></i>{chapter['short']}</a><a class="l" href="#top">{num}</a>
  <a class="l" href="#why">왜</a><a class="l" href="#big">큰 그림</a>{navlinks}
  <a class="l" href="#duel">대결</a><a class="l" href="#summary">정리</a><a class="l" href="#kg">지식 색인</a><a class="l" href="#export">꾸러미</a>
</nav>

<header class="hero" id="top">
  <div class="hex"></div>
  <div class="hero-bg" data-img="bg_{P['key']}" role="img" aria-label="{P['hero_alt']}"><canvas id="heroCv" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <div class="hero-text">
      <div class="eyebrow">{chapter['eyebrow']} · {num}</div>
      <h1>{P['h1']}</h1>
      <p class="q">{P['question']}</p>
      <p class="lead">{P['lead']}</p>
    </div>
    {kpi_html(P['kpis'])}
    <div class="dialog" aria-label="캐릭터 대화">{hero_dialog}</div>
  </div>
</header>

<section class="level" id="cast"><div class="wrap">
  <h2>등장인물 · 이 페이지 사용법</h2>
  <div class="cast">{cast}</div>
  <p class="sub">노란 점선 밑줄을 누르면 뜻이 나와요(오른쪽 아래 도우미에서 핵심 → 전체 → 끄기). 그림 안 노란 도장이 붙은 숫자는 원리를 보이려고 만든 예시값이고, 각주 [n]이 붙은 숫자만 자료에서 옮긴 값이에요.</p>
</div></section>

<section class="level" id="why"><div class="wrap">
  <h2>{P['why_title']}</h2>
  <p class="sub">{P['why_lead']}</p>
  <div class="steps">{steps}</div>
  {say(*P['why_say'])}
</div></section>

<section class="level" id="big"><div class="wrap">
  <h2>큰 그림 — {chapter['title']}의 {idx+1}번째 칸</h2>
  <nav class="path" aria-label="챕터 안 위치">{path}</nav>
  <p class="sub">{P['big_lead']}</p>
  <div class="tw"><table class="tb">
    <thead><tr><th>칸</th><th>방식</th><th>새로 생긴 능력</th><th>이 칸의 한계 → 다음 칸</th></tr></thead>
    <tbody>{ladder_rows}</tbody></table></div>
  {say(*P['big_say']) if P.get('big_say') else ''}
</div></section>
{rungs}

<section class="level" id="duel"><div class="wrap">
  <h2>대결 — {D['title']}</h2>
  <p class="sub">{D['intro']}</p>
  <div class="duel" id="duelBox">
    <div class="duelhead">
      <div><img data-who="fly" data-mood="point" data-img="fly_e08" data-face="right" alt="" aria-hidden="true"><div style="color:var(--c-fly);font-weight:700">초파리 연구원</div></div>
      <div class="vs">VS</div>
      <div><img data-who="robo" data-mood="coin" data-img="robo_e16" data-face="left" alt="" aria-hidden="true"><div style="color:var(--c-robo);font-weight:700">주판봇</div></div>
    </div>
    <div class="choices">
      <div class="choice fly"><b>초파리의 선택: {D['fly'][0]}</b><p>"{D['fly'][1]}"</p><p class="sub" style="margin:0">{D['fly'][2]}</p></div>
      <div class="choice robo"><b>주판봇의 선택: {D['robo'][0]}</b><p>"{D['robo'][1]}"</p><p class="sub" style="margin:0">{D['robo'][2]}</p></div>
    </div>
    <div class="guess" role="group" aria-label="먼저 맞혀 보기">
      <button class="bt" data-g="F" aria-pressed="false">초파리가 이길 것 같다</button>
      <button class="bt" data-g="R" aria-pressed="false">주판봇이 이길 것 같다</button>
      <button class="bt" data-g="D" aria-pressed="false">비길 것 같다</button>
    </div>
    <div style="text-align:center"><button class="bt primary reveal">결과 보기</button></div>
    <div class="after">
      <div class="score"><span class="f">초파리 <i id="scF">0</i></span><span class="r">주판봇 <i id="scR">0</i></span></div>
      <div class="bars" aria-live="polite"></div>
      {say('asst','firm','asst_e12','—','asst')}
      {say('doc','judge','doc_e10','—','verdict')}
      <p id="guessFb" class="sub"></p>
      {D.get('after','')}
    </div>
  </div>
  {D.get('math','')}
</div></section>

<section class="level" id="summary"><div class="wrap">
  <h2>정리</h2>
  {P['summary']}
  {say(*P['summary_say'])}
</div></section>

<section class="level" id="outro"><div class="wrap">
  <h2>아웃트로</h2>
  <div class="stage" data-img="sc_{P['key']}_outro" role="img" aria-label="{P['outro_alt']}">{stage}</div>
  {outro}
</div></section>

<section class="level" id="kg"><div class="wrap">
  <h2>지식 색인 — 이 페이지에서 찾아보기</h2>
  <p class="sub" id="kgStats"></p>
  <div class="kgtools"><input type="text" id="kgQ" placeholder="검색: {P['kg_hint']}" aria-label="지식 색인 검색"><div id="kgChips" role="group" aria-label="종류 필터"></div></div>
  <div class="flow" id="kgPath" aria-label="사다리 경로"></div>
  <div class="kggrid">
    <div class="kglist" id="kgList" aria-live="polite"></div>
    <div>
      <div class="cwrap"><canvas id="kgCv" aria-label="이 페이지 개념들의 관계 그래프. 노드를 누르면 목록에서 펼쳐진다"></canvas></div>
      <div class="legend" id="kgLegend"></div>
      <h3>열린 질문</h3><ul id="kgOpen"></ul>
      <div class="ctrl"><div class="group"><button class="bt" id="kgJson">JSON 내려받기</button><button class="bt" id="kgMmd">Mermaid 내려받기</button></div><span class="glabel">전체 형식은 아래 꾸러미에서</span></div>
    </div>
  </div>
</div></section>

<section class="level" id="export"><div class="wrap">
  <h2>온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기</h2>
  <section class="kpis" id="exK"></section>
  <h3>이 페이지 인용하기</h3>
  <div class="group"><button class="chip" data-cf="text" aria-pressed="true">일반 문장</button><button class="chip" data-cf="bib" aria-pressed="false">BibTeX</button><button class="chip" data-cf="ris" aria-pressed="false">RIS</button><button class="bt" id="exCopy">복사</button></div>
  <pre class="cite" id="exCite"></pre>
  <h3>참고문헌</h3><div class="reflist" id="exRefs"></div>
  <h3>범위와 형식 고르기</h3>
  <div class="group" role="group" aria-label="범위"><button class="chip" data-sc="all" aria-pressed="true">전체</button><button class="chip" data-sc="concepts" aria-pressed="false">개념·방법만</button><button class="chip" data-sc="claims" aria-pressed="false">주장 + 출처만</button><button class="chip" data-sc="prereq" aria-pressed="false">선수 관계만</button></div>
  <div class="ctrl"><div class="group"><button class="bt primary" id="exZip">꾸러미 ZIP 내려받기</button></div></div>
  <div class="group" id="exFiles"></div>
  <div id="dlBox" class="panel"><h3 id="dlName">파일 내용</h3><p class="sub" style="margin:0">내려받기가 막힌 화면에서는 아래 내용을 복사해 같은 이름의 파일로 저장하세요.</p><div class="ctrl"><button class="bt" id="dlCopy">내용 복사</button><button class="bt" id="dlClose">닫기</button></div><pre class="cite" id="dlText"></pre></div>
  <h3>확인 필요 목록</h3><ul id="exTodo"></ul>
  <p class="sub" id="exVer"></p>
  {say('asst','ledger','asst_e07','<span id="exSay">출처 없는 주장은 꾸러미에 넣지 않았어요.</span>')}
</div></section>

<footer><div class="wrap">
  <h3>출처</h3><ol>{refs_li}</ol>
  <p>캐릭터 그림: adminmrobo/fruitfly-lab-expressions (ea5da3f)</p>
  <h3>예시값·설명용 모형인 것</h3><ul>{ex_li}</ul>
  <p class="pn">{pn} · <a href="index.html">{chapter['short']} 목차</a> · {nn}</p>
  <p>저자: 안상선 · {M['series']} {num} · v{M['version']} · {M['date']}</p>
</div></footer>

<div id="tip" role="tooltip"></div>
<div id="study" aria-live="polite"><span id="stTxt">읽은 곳 0% · 퀴즈 0/0</span><button id="stBtn">밑줄: 핵심</button></div>
<script type="application/json" id="gloss-data">{js(P['gloss'])}</script>
<script type="application/json" id="quiz-data">{js(P['quiz'])}</script>
<script type="application/json" id="kg-raw">{js(P['kg'])}</script>
<script type="application/ld+json" id="kg-ld">{js(P['ld'])}</script>
<script type="application/json" id="refs-csl">{js(P['refs'])}</script>
<script type="application/json" id="page-meta">{js(P['meta'])}</script>
<script src="{assets}sprites.js"></script>
<script src="{assets}lab.js"></script>
<script>
{P['js']}
</script>
</body></html>'''
