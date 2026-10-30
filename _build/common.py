"""Shared data and builders for chapter 1 pages."""
DATE = "2026-10-29"
SERIES = "연구실 해설 대시보드 · 블록체인 편 2장 「블록체인 기술」"
LEC_ID = "lecture2024blockchain"
WP_ID = "nakamoto2008bitcoin"

REFS_ALL = {
 LEC_ID: {"id": LEC_ID, "type": "report", "title": "4차산업시대의 금융: 블록체인의 원리 · 블록체인 서비스 사례 · 블록체인과 비트코인 (강의 교안)",
   "issued": {"date-parts": [[2024, 10, 18]]}, "number-of-pages": "45",
   "lab": {"work": "lab:work/" + LEC_ID, "role": "primary",
     "verified": {"title": True, "authors": False, "year": False, "venue": False, "doi": False, "pages": True},
     "checkedBy": "사용자가 준 PDF 직접 확인 2026-10-28",
     "note": "저자·기관 표기 없음. 연도는 PDF 생성일(2024-10-18) 기준이며 강의 연도 확인 필요"}},
 WP_ID: {"id": WP_ID, "type": "report", "title": "Bitcoin: A Peer-to-Peer Electronic Cash System",
   "author": [{"family": "Nakamoto", "given": "Satoshi"}], "issued": {"date-parts": [[2008]]},
   "URL": "https://bitcoin.org/bitcoin.pdf", "accessed": {"date-parts": [[2026, 10, 29]]},
   "lab": {"work": "lab:work/" + WP_ID, "role": "primary",
     "verified": {"title": True, "authors": True, "year": True, "venue": True, "doi": False, "pages": False, "url": False},
     "checkedBy": "본문 확인: 대학 강의 자료실 사본(cs-web.bu.edu) 2026-10-28·29",
     "note": "공식 주소(bitcoin.org)는 이 세션에서 직접 열지 못함. DOI 없음(백서)"}},
 "seoul2019perjury": {"id": "seoul2019perjury", "type": "article-newspaper", "title": "매년 3000여건 거짓 증언, 사법 정의 흔든다",
   "container-title": "서울신문", "issued": {"date-parts": [[2019, 6, 9]]},
   "lab": {"work": "lab:work/seoul2019perjury", "role": "data",
     "verified": {"title": False, "authors": False, "year": False, "venue": False, "doi": False, "pages": False, "url": False},
     "checkedBy": "강의 교안 p.10의 그림 출처 표기로만 확인 (원문 미확인)", "note": "원 기사 확인 필요"}},
}
WORK_LABEL = {LEC_ID: ("강의 교안: 블록체인의 원리", "Lecture notes: principles of blockchain", "#ref1"),
              WP_ID: ("Bitcoin: A Peer-to-Peer Electronic Cash System", "Bitcoin white paper", "#ref2"),
              "seoul2019perjury": ("서울신문: 매년 3000여건 거짓 증언", "Seoul Shinmun on perjury", "#ref3")}

# 용어: key -> (표제, 분류, 설명, node id, node type, anchor-default)
GLOSS_ALL = {
 "장부": ("장부 (ledger)", "기록", "거래가 언제, 누구에서 누구에게, 얼마였는지 적어 두는 기록.", "lab:concept/ledger", "Concept"),
 "블록체인": ("블록체인 (blockchain)", "구조", "거래 기록을 블록 단위로 묶어 사슬처럼 이은 분산원장. 모든 참여자가 함께 저장·검증한다.", "lab:concept/blockchain", "Concept"),
 "분산원장": ("분산원장 (distributed ledger)", "구조", "같은 거래 장부를 네트워크 참여자들이 각자 한 부씩 저장하고 함께 검증하는 방식.", "lab:method/distributed-ledger", "Method"),
 "비트코인": ("비트코인 (Bitcoin)", "화폐", "블록체인 기술을 바탕으로 한 디지털 화폐. 2008년 논문으로 소개되고 2009년 처음 발행됐다.", "lab:concept/bitcoin", "Concept"),
 "백서": ("백서 (white paper)", "문헌", "여기서는 사토시 나카모토의 논문 'Bitcoin: A Peer-to-Peer Electronic Cash System'을 가리킨다.", "lab:term/white-paper", "Term"),
 "이중 지불": ("이중 지불 (double-spending)", "문제", "같은 디지털 돈을 두 번 이상 쓰는 것. 파일은 복사되므로 누가 이미 썼는지 확인할 장치가 필요하다.", "lab:concept/double-spending", "Concept"),
 "중개자": ("중개자 (trusted third party)", "구조", "거래 당사자 사이에서 기록을 맡고 확인해 주는 제3자. 은행, 공증인 등.", "lab:concept/trusted-third-party", "Concept"),
 "중앙집중식": ("중앙집중식 시스템", "구조", "장부와 처리를 한 곳(중앙 서버·기관)이 맡는 구조. 빠르지만 그곳이 멈추면 전체가 멈춘다.", "lab:method/centralized-network", "Method"),
 "단일 실패 지점": ("단일 실패 지점 (single point of failure)", "구조", "그 한 곳이 멈추거나 뚫리면 시스템 전체가 멈추는 지점.", "lab:limitation/single-point-of-failure", "Limitation"),
 "노드": ("노드 (node)", "구조", "네트워크에 연결된 참여자 한 명(컴퓨터 한 대). 블록체인에서는 장부 사본을 저장하고 검증한다.", "lab:term/node", "Term"),
 "홉": ("홉 (hop)", "지표", "메시지가 한 노드에서 이웃 노드로 한 번 건너가는 것. 홉 수가 적을수록 빨리 도착한다.", "lab:metric/average-hops", "Metric"),
 "간인": ("간인", "제도", "여러 장으로 된 문서의 장과 장 사이에 걸쳐 찍는 도장. 중간 장을 바꿔치기하면 도장이 어긋난다.", "lab:term/ganin", "Term"),
 "접인": ("접인", "제도", "계약서 두 부를 겹쳐 놓고 양쪽에 걸쳐 찍는 도장. 두 부가 같은 때 같이 만든 것임을 보인다.", "lab:term/jeobin", "Term"),
 "병기": ("병기 (숫자·한글)", "제도", "금액을 숫자와 한글로 함께 적는 것. 한쪽만 고치면 두 표기가 어긋나 위조가 드러난다.", "lab:method/dual-notation", "Method"),
 "공증": ("공증 (notarization)", "제도", "특정 사실이나 법률관계를 법률상 권한 있는 사람이 공적으로 증명하고 서명·날인하는 일.", "lab:method/notarization", "Method"),
 "위증": ("위증 (perjury)", "제도", "법정에서 증인이 거짓으로 증언하는 일. 처벌 대상이다.", "lab:term/perjury", "Term"),
 "다수결": ("다수결 (majority vote)", "합의", "여러 증인 또는 장부 중 절반을 넘는 쪽의 기록을 사실로 정하는 방법.", "lab:concept/majority-vote", "Concept"),
 "과반": ("과반 (majority)", "합의", "전체의 절반을 넘는 수. N권 중 ⌊N/2⌋+1권.", "lab:concept/majority-vote", "Concept"),
 "수수료": ("수수료 (fee)", "비용", "기관이 거래·서류 발급·계좌 관리의 대가로 받는 돈. 믿음을 유지하는 비용이 소비자에게 돌아온 것.", "lab:concept/fee", "Concept"),
 "공인인증서": ("공인인증서", "인증", "정부 인증 기관과 여러 중개 기관이 참여하는 체계로 신원을 확인하는 전자 인증서. 강의 자료의 표기를 따름.", "lab:method/certificate-auth", "Method"),
 "OTP": ("OTP (일회용 비밀번호)", "인증", "한 번만 쓰는 비밀번호를 만들어 서버가 확인하는 인증 방식.", "lab:method/otp", "Method"),
 "가용성": ("가용성 (availability)", "지표", "시스템이 필요할 때 실제로 동작하고 있는 시간의 비율.", "lab:metric/availability", "Metric"),
 "가짜 노드": ("가짜 노드 (Sybil)", "보안", "한 사람이 여러 참여자인 척 만든 노드. 사람 수로 투표하는 망을 무너뜨릴 수 있다.", "lab:concept/sybil", "Concept"),
 "블록": ("블록 (block)", "구조", "거래 기록을 묶어 저장하는 단위. 자기 데이터와 이전 블록의 해시를 함께 담는다.", "lab:concept/block", "Concept"),
 "블록 헤더": ("블록 헤더 (block header)", "구조", "블록의 요약 정보(이전 블록 해시, 시각, 논스 등). 비트코인 백서 기준 거래 없이 약 80바이트.", "lab:term/block-header", "Term"),
 "해시": ("해시 (hash)", "암호", "임의 길이의 데이터를 고정 길이 문자열로 바꾸는 단방향 함수의 결과. 입력이 조금만 바뀌어도 전혀 다른 값이 나온다.", "lab:concept/hash-function", "Concept"),
 "SHA-256": ("SHA-256", "암호", "비트코인이 쓰는 해시 함수. 결과는 256비트(16진수 64자).", "lab:term/sha-256", "Term"),
 "눈사태 효과": ("눈사태 효과 (avalanche effect)", "암호", "입력이 조금만 바뀌어도 해시값의 대부분이 바뀌는 성질.", "lab:concept/avalanche-effect", "Concept"),
 "단방향": ("단방향성 (one-way)", "암호", "해시값에서 원본을 거꾸로 계산할 수 없는 성질. 단, 입력 후보가 적으면 전부 대입해 찾을 수 있다.", "lab:concept/one-wayness", "Concept"),
 "솔트": ("솔트 (salt)", "암호", "해시하기 전에 원문에 덧붙이는 무작위 문자열. 입력 후보를 크게 늘려 대입 공격을 막는다.", "lab:method/salting", "Method"),
 "타임스탬프": ("타임스탬프 (timestamp)", "구조", "데이터가 그 시각에 존재했음을 보이는 기록. 백서는 각 타임스탬프가 이전 타임스탬프를 해시에 포함해 사슬을 이룬다고 설명한다.", "lab:term/timestamp", "Term"),
 "무결성": ("무결성 (integrity)", "보안", "데이터가 허락 없이 바뀌지 않았음이 보장되는 성질.", "lab:concept/integrity", "Concept"),
 "데이터베이스": ("데이터베이스 (database)", "구조", "대량의 데이터를 중앙 시스템에서 효율적으로 저장·검색·수정하도록 관리하는 체계.", "lab:method/database", "Method"),
 "이력": ("이력 (history)", "기록", "데이터가 바뀌어 온 전체 과정. 블록체인은 현재 값보다 변화의 이력을 시간 순서대로 쌓는다.", "lab:concept/history-record", "Concept"),
 "이력 관리": ("이력 관리 (provenance tracking)", "활용", "생산·가공·유통 단계의 기록을 블록체인에 남겨 위변조를 막고 추적하게 하는 활용.", "lab:concept/provenance-tracking", "Concept"),
 "채굴": ("채굴 (mining)", "채굴", "새 블록을 만들고 검증하는 계산 작업. 먼저 성공한 채굴자가 보상으로 비트코인을 받는다.", "lab:concept/mining", "Concept"),
 "채굴 보상": ("채굴 보상 (block reward)", "채굴", "새 블록을 만든 채굴자가 받는 비트코인. 블록의 첫 거래로 새 코인이 만들어진다.", "lab:concept/block-reward", "Concept"),
 "논스": ("논스 (nonce)", "채굴", "'일회성 숫자'. 채굴할 때 해시가 목표보다 작아질 때까지 바꿔 가며 넣는 값.", "lab:term/nonce", "Term"),
 "채굴 난이도": ("채굴 난이도 (mining difficulty)", "채굴", "채굴 문제의 어려운 정도. 참여 계산력이 늘면 올라가고 줄면 내려가, 정해진 시간에 일정 수의 블록이 나오게 한다.", "lab:concept/mining-difficulty", "Concept"),
 "작업증명": ("작업증명 (Proof of Work)", "합의", "계산 작업을 해냈다는 증거(목표보다 작은 해시)로 블록 생성 권한을 정하는 합의 방식.", "lab:method/proof-of-work", "Method"),
 "계산력": ("계산력 (hash rate)", "채굴", "채굴에 쓰는 장비가 1초에 계산하는 해시의 수. 블록을 먼저 찾을 확률은 계산력 몫에 비례한다.", "lab:metric/hash-rate", "Metric"),
 "목표값": ("목표값 (target)", "채굴", "블록 해시가 이 값보다 작아야 유효하다. 목표값이 작을수록 난이도가 높다.", "lab:term/target", "Term"),
 "확정": ("확정 (confirmation)", "합의", "거래가 담긴 블록 뒤에 블록이 더 쌓여 되돌리기 어려워지는 것. 쌓인 블록 수로 센다.", "lab:concept/confirmation-depth", "Concept"),
 "가장 긴 사슬": ("가장 긴 사슬 (longest chain)", "합의", "작업증명이 가장 많이 들어간 사슬. 백서는 다수의 결정을 이 사슬로 표현한다.", "lab:concept/longest-chain", "Concept")
}

CANON = {'lab:concept/majority-vote': ('과반 다수결', 'majority vote')}
QUIZ_KEYS = ("q", "o", "a", "why", "hint")

def L(ko, en): return {"ko": ko, "en": en}

def build(P, num, slug, family="systems"):
    """P['kgspec'] -> P['kg'], P['ld'], P['refs'], P['gloss'], P['meta']"""
    S = P['kgspec']; page = f"{num}_{slug}"
    N, E, ids = [], [], set()
    def node(id, type, ko, en, anchor, d=None, level=None, src=None, alt=None, conf="high", ev=None):
        if id in ids: return
        n = {"id": id, "type": type, "label": L(ko, en), "page": page, "anchor": anchor, "family": family,
             "anchorType": P['anchor'], "flyStrength": "none", "status": "known", "confidence": conf, "coverage": "explained"}
        if d: n["definition"] = {"ko": d}
        if level: n["level"] = level
        if src: n["source"] = [{"cite": c, "loc": l} for c, l in src]
        if alt: n["altLabel"] = {"ko": alt}
        if ev: n["evidence"] = ev
        n["match"] = [{"scheme": "wikidata", "id": "", "rel": "closeMatch", "verified": False}]
        N.append(n); ids.add(id)
    def edge(s, p, o, a, conf="high", ev=None):
        e = {"s": s, "p": p, "o": o, "anchor": a, "confidence": conf}
        if ev: e["evidence"] = ev
        E.append(e)
    for t in S['nodes']:
        node(*t)
    # glossary nodes
    gl = []
    for key, core in P['gloss_keys']:
        g = GLOSS_ALL[key]
        ko, en = CANON.get(g[3], (g[0].split(' (')[0], g[0].split('(')[-1].rstrip(')') if '(' in g[0] else g[0]))
        node(g[3], g[4], ko, en, P['gloss_anchor'].get(key, '#top'), g[2])
        gl.append([key, g[0], g[1], g[2], g[3], P['gloss_anchor'].get(key, '#top'), core])
    used = set()
    for cid, ko, anc, sup, srcs, fc in S['claims']:
        node(cid, "Claim", ko, cid.split('/')[1], anc, src=srcs, ev=[fc])
        for s in sup: edge(cid, "lab:supports", s, anc, ev=[fc])
        for c, l in srcs:
            used.add(c); edge(cid, "lab:assertedIn", "lab:work/" + c, anc, ev=[fc])
    for n in list(N):
        for s in n.get("source", []): used.add(s["cite"])
    order = P.get('ref_order', [LEC_ID, WP_ID, "seoul2019perjury"])
    order = [c for c in order if c in used] + sorted(c for c in used if c not in order)
    for i, c in enumerate(order):
        ko, en, a = WORK_LABEL[c]; node("lab:work/" + c, "Work", ko, en, f"#ref{i+1}")
    for sid, ko, anc, cs in S['sims']:
        node(sid, "Simulation", ko, sid.split('/')[1], anc)
        for c in cs: edge(c, "lab:demonstratedBy", sid, anc)
    for t in S['edges']:
        edge(*t)
    for sec, items in P['quiz'].items():
        for i, q in enumerate(items):
            qid = f"lab:quiz/{num}-{sec}-{i+1}"
            node(qid, "QuizItem", q['q'], f"quiz {num} {sec}-{i+1}", "#" + sec)
            edge(qid, "lab:assesses", q['c'], "#" + sec)
    # checks
    for e in E:
        assert e['s'] in ids and e['o'] in ids, (num, e)
    deg = {i: 0 for i in ids}
    for e in E: deg[e['s']] += 1; deg[e['o']] += 1
    iso = [i for i, d in deg.items() if d == 0]
    assert not iso, (num, iso)
    rel = sum(1 for e in E if e['p'] == 'lab:relatedTo') / max(1, len(E))
    assert rel <= 0.15, (num, rel)
    P['kg'] = {"version": "1.0", "page": page, "created": DATE, "registry": "KG_00_registry (블록체인 편 v0.2, 1·2장)", "ladder": S['ladder'], "nodes": N, "edges": E}
    P['gloss'] = gl
    refs = []
    for c in [LEC_ID, WP_ID, "seoul2019perjury"]:
        if c in used:
            r = dict(REFS_ALL[c]); lab = dict(r['lab'])
            sup = [cl[0] for cl in S['claims'] if any(x[0] == c for x in cl[4])]
            lab['supports'] = sup
            lab['locs'] = [{"claim": cl[0], "loc": [l for x, l in cl[4] if x == c][0]} for cl in S['claims'] if any(x[0] == c for x in cl[4])]
            r['lab'] = lab; refs.append(r)
    P['refs'] = refs
    ctx = {"skos": "http://www.w3.org/2004/02/skos/core#", "schema": "https://schema.org/", "dct": "http://purl.org/dc/terms/", "prov": "http://www.w3.org/ns/prov#", "lab": "urn:lab:"}
    PM = {"lab:broader": "skos:broader", "lab:partOf": "dct:isPartOf", "lab:relatedTo": "skos:related", "lab:assertedIn": "schema:citation"}
    graph = {}
    for n in N:
        o = {"@id": n["id"], "@type": ["skos:Concept", "lab:" + n["type"]], "skos:prefLabel": [{"@value": n["label"]["ko"], "@language": "ko"}, {"@value": n["label"]["en"], "@language": "en"}]}
        if "definition" in n: o["skos:definition"] = {"@value": n["definition"]["ko"], "@language": "ko"}
        graph[n["id"]] = o
    for e in E:
        g = graph[e["s"]]; g.setdefault(e["p"], []).append({"@id": e["o"]})
        if e["p"] in PM: g.setdefault(PM[e["p"]], []).append({"@id": e["o"]})
    P['ld'] = {"@context": ctx, "@graph": list(graph.values())}
    P['meta'] = {"title": P['meta_title'], "series": SERIES, "number": num, "citekey": "ahn2026blockchain" + num.replace('-', ''),
        "creator": [{"name": "안상선", "role": "author"}], "contributor": [{"name": "AI 보조 제작 (Claude)", "role": "assistant"}],
        "date": DATE, "version": "1.0", "language": ["ko"], "license": "", "url": "",
        "about": S['about'], "educationalLevel": "입문~중급", "learningResourceType": "interactive explainer",
        "basedOn": sorted(used),
        "suggestedCitation": f"안상선 (2026). {P['meta_title']}. {SERIES} {num}, v1.0."}
    return len(N), len(E)
