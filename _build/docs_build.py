import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SRC = ROOT + '/src'
STYLE = "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents"
NEG = "no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands"
CORE = {
 'doc': "the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks",
 'asst': "Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat",
 'fly': "the Fruit Fly, a tiny expressive cartoon fruit fly researcher with a dark charcoal-black segmented insect body, large glossy red compound eyes, a retro dark blue helmet with a yellow-white center stripe and small round side bolts, colorful dangling cables in magenta, purple and blue curving from the back of the helmet, a tiny white lab coat over a black vest, translucent veined wings, six thin black legs with the front pair used like hands",
 'robo': "MONEY-ROBO, a cute small floating chibi robot with a large glossy rounded-square white head and a small rounded white body with thick black outlines, a black pill-shaped screen face showing golden-yellow pixel eyes and mouth, a small round knob antenna on a short stem, stubby rounded fingerless arms, no legs, a black oval chest panel with a bright cyan pill-shaped core light, hovering above a small dark oval shadow"}
PAGES = {
 '2-01': ('C', '회계실 포장대: 거래 쪽지 묶음을 상자에 담고 상자마다 머리표를 다는 곳', "cozy accounting room beside the lab, a packing table where many small blank paper slips are bundled with string and placed into wooden crates, each crate has a blank brass header tag on its lid, a conveyor of crates moving to the right, stacks of gold coins, warm golden lamp light", '거래 쪽지를 묶어 상자에 담는 회계실 포장대', 'R', [('robo','happy'),('fly','coffee')], "MONEY-ROBO in front raising both arms beside a full crate of bundled slips, the Fruit Fly behind holding a coffee cup with a calm accepting look"),
 '2-02': ('D', '감식 책상: 지문 카드, 돋보기, 봉인된 봉투들', "a forensic desk in the same night lab world, blank fingerprint cards under a big magnifying glass, a row of sealed envelopes each with a different abstract swirl pattern, a small brass lock with a four-wheel dial, purple lab light spilling in from one side", '지문 카드와 돋보기, 봉인된 봉투가 놓인 감식 책상', 'F', [('fly','arms'),('robo','sigh')], "the Fruit Fly in front with arms crossed holding a magnifying glass, MONEY-ROBO behind with a sweat drop beside an opened four-wheel dial lock"),
 '2-03': ('C', '금고실 진열대: 장부 쪽이 놋쇠 사슬로 차례로 이어진 진열대', "a bank vault room beside the lab, a long display stand where six blank ledger pages hang in a row linked one to the next by brass chain links, one link in the middle glowing red as if broken, a huge round vault door in the back, warm golden lamp light", '놋쇠 사슬로 이어진 장부 쪽 여섯 장이 걸린 금고실 진열대', 'X', [('fly','arms'),('robo','blush')], "the Fruit Fly in front with arms crossed beside the chained ledger pages, MONEY-ROBO behind with pink blush lines and a small yellow warning triangle on its face screen"),
 '2-04': ('D', '사무실 기록실: 지웠다 다시 쓰는 칠판과 바닥까지 늘어진 긴 영수증 두루마리', "an office records room in the same night lab world, on the left a small chalkboard with smudged erased marks and an eraser, on the right a very long blank receipt paper roll unrolling from a desk down to the floor in loops, filing cabinets, purple lab light spilling in from one side", '지운 자국이 남은 칠판과 바닥까지 늘어진 영수증 두루마리', 'R', [('robo','happy'),('fly','cry')], "MONEY-ROBO in front raising both arms beside a neat small chalkboard, the Fruit Fly behind with waterfall tears tangled in a long paper roll but nodding in acceptance"),
 '2-05': ('D', '냉장 창고와 축사 문: 생선 상자와 꼬리표, 단계별 검수대', "a cold storage warehouse in the same night lab world, stacked fish crates on ice with small blank tags tied to each crate, a wooden barn door to a cattle shed in the background, five small inspection stands in a row from left to right, cool blue light mixed with purple lab light", '꼬리표 달린 생선 상자와 단계별 검수대가 있는 냉장 창고', 'F', [('fly','arms'),('robo','sigh')], "the Fruit Fly in front with arms crossed holding a clipboard beside the inspection stands, MONEY-ROBO behind with a sweat drop holding a single blank label"),
 '2-06': ('C', '채굴실: 번호 자물쇠 상자들, 빛나는 채굴 장비, 금화 더미', "a mining room beside the accounting room, many small locked boxes with combination dials on shelves, glowing cyan mining machines with fans, piles of gold coins being dropped into four separate trays, warm golden lamp light", '번호 자물쇠 상자와 빛나는 채굴 장비, 금화 더미가 있는 채굴실', 'R', [('robo','happy'),('fly','cry')], "MONEY-ROBO in front raising both arms beside four glowing mining machines and a big coin tray, the Fruit Fly behind with waterfall tears beside a single small machine but nodding in acceptance"),
 '2-07': ('C', '시계탑 회계실: 큰 모래시계와 높이가 다른 장부 두 더미', "an accounting room inside a clock tower beside the lab, a large brass hourglass in the center, two stacks of leather ledgers on a table, one tall stack glowing green and one short stack in shadow, a big round clock face without numbers on the wall, warm golden lamp light", '큰 모래시계와 높이가 다른 장부 두 더미가 놓인 시계탑 회계실', 'F', [('fly','arms'),('robo','sigh')], "the Fruit Fly in front with arms crossed beside the tall stack of ledgers and the hourglass, MONEY-ROBO behind with a sweat drop beside the short stack"),
}
SLUG = {}
for f in os.listdir(ROOT):
    m = re.match(r'(2-0\d)_(.+)\.html', f)
    if m: SLUG[m.group(1)] = (m.group(2), f)
manifest_all = []
for num, (anc, place_ko, place_en, alt_bg, res, (a, b), outro_en) in PAGES.items():
    slug, fn = SLUG[num]; key = num.replace('-', '_'); html = open(os.path.join(ROOT, fn)).read()
    info = json.load(open(os.path.join(SRC, f'info_{num}.json')))
    packs = sorted(set(re.findall(r'data-img="((?:doc|asst|fly|robo)_e\d\d)"', html)))
    bg_prompt = f"{STYLE}, wide 8:3 background, left side simple and calm for title text, details on the right, {place_en}, no characters, {NEG}"
    chars = [w for w in ['fly', 'robo', 'doc', 'asst'] if w in ('fly', 'robo') or w in outro_en.lower() or w == 'asst']
    outro_prompt = f"{STYLE}, 3:2 landscape scene, medium brightness, {place_en}, " + '; '.join(CORE[w] for w in ['fly','robo','doc','asst']) + f"; composition: {outro_en}; the winner is in front and larger, the other side shows an accepting gesture, no mocking, {NEG}"
    res_ko = {'F': '초파리 승', 'R': 'Money-Robo 승', 'D': '무승부', 'X': 'Money-Robo 실격'}[res]
    rows = [f"| 1 | bg_{key} | F | 1920×720 | 의뢰 | 외부 | P1 | 히어로 배경 | 픽셀 코드 배경 ({'금고·금화·로봇' if anc=='C' else '책상·서류·두 사람'}) |",
            f"| 2 | sc_{key}_outro | E | 1200×800 | 넣음 (합성본) | 직접 → 외부 선택 | P2 | 아웃트로 무대 | 팩 캐릭터 4명 CSS 무대 |",
            f"| 3 | thumb_{key} | I | 600×400 | 넣음 (합성 방법 지정) | 직접 | P2 | 목차 카드 | bg_{key}을 3:2로 자르기 |",
            f"| 4 | og_{key} | K | 1200×630 | 넣음 (합성 방법 지정) | 직접 | P3 | 공유 미리보기 | CSS 배경 + fly_e08·robo_e16 + 제목 |"]
    for i, k in enumerate(packs): rows.append(f"| {5+i} | {k} | {'ABCD'[['doc','asst','fly','robo'].index(k.split('_')[0])]} | 팩 96{'·192' if k in ('fly_e08','robo_e16','fly_e16','robo_e14','robo_e12','fly_e13','fly_e21','robo_e18','robo_e20','doc_e08','asst_e16','asst_e13') else ''} | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |")
    md = f"""# {num} 「{info['title']}」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | {fn} |
| 모드 / 주 앵커 | 교과서 / {anc} {'장부' if anc=='C' else '생활·현장'}: {place_ko} |
| 시즌 | 기본 |
| 대결 | {info['duel']} → 결과 **{res}** ({res_ko}) |
| 새로 그릴 그림 | P1 1장 · P2 2장 · P3 1장 |
| 제작 경로 | 직접 3장 (합성본·합성 방법) · 외부 의뢰 1장 (+ 선택 1장) |
| 의뢰 도구 | Genspark (기본) |
| 진행 | 받음 0 / 의뢰 1 · 마지막 반영 아직 |
| 캐릭터 팩 표정 | {len(packs)}장 + 대결 결과용 역할 키 (팩 커밋 ea5da3f, 공용 assets/sprites.js) |
| 그림이 없을 때 | 페이지는 캐릭터 팩 표정, 픽셀 코드 히어로, CSS 무대로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 · 캐릭터 고정 외형: SKILL 18-4 (공식 저장소 `CHARACTER_CORE_EN`)
- 이 페이지 장소: {place_ko}
- 장소 영어 묘사: *{place_en}*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 제작 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|---|
""" + '\n'.join(rows) + f"""

대결 결과용 표정(fly_arms·fly_coffee·fly_cry·robo_happy·robo_sigh·robo_meh·robo_blush·asst_firm·asst_spark·asst_shock·doc_judge·doc_scale)은 공용 sprites.js에 들어 있다. doc_scale은 그림 없음 → doc_e13 (P2 새 표정 후보, 시리즈 공용 명세서 참고).

## 3. 새로 그릴 그림 상세

### 3-1. `bg_{key}` — 대표 배경
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 |
| 제작 경로 | 외부: Genspark |
| 구도 | 왼쪽 45%는 단순한 어두운 벽·바닥(제목 자리), 오른쪽에 장소 소품 |
| 피할 것 | 글자·숫자·₿·실제 화폐 무늬, 실존 은행·기관 로고, 인물 |
| 대체 글 (alt) | {alt_bg} |

```
{bg_prompt}
```

### 3-2. `sc_{key}_outro` — 아웃트로 장면 (선택)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 제작 경로 | 지금: 팩 캐릭터 CSS 무대 합성(페이지에 있음) → 외부 의뢰 선택 |
| 구도 | {outro_en} |
| 대체 글 (alt) | 페이지 `.stage`의 aria-label과 같음 |

```
{outro_prompt}
```

### 3-3. `thumb_{key}`, `og_{key}` — 직접 합성
- thumb: bg_{key}을 받으면 오른쪽 소품 부분을 3:2로 자른다. 받기 전에는 CSS 배경 + 팩 캐릭터 1명.
- og: 배경 + fly_e08(오른쪽 봄)·robo_e16(왼쪽 봄) 192px + 제목 글자(HTML·SVG).

## 4. 일관성 지침
- 참고 이미지: 저장소 `refs/original/keyart_rivals.png` + 장면에 나오는 캐릭터의 원본 표정 PNG
- 같은 챕터 그림은 한 도구·한 세션에서 2-01 → 2-07 순서로 (배경 7장 먼저, 장면은 그다음)
- 투명 배경이 안 되면 *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
SKILL 18-15. `python3 build_character_pack.py --ingest 받은폴더/ --plates bg_{key}=F,sc_{key}_outro=E --out received_{key}` → 결과 조각을 `assets/` 쪽 공용 파일이 아니라 이 페이지 스크립트의 `Object.assign(SPRITE,...)`로 넣는다(배경은 페이지마다 다르므로).

## 6. 체크리스트
- [x] HTML의 모든 `data-img` 키가 이 명세서에 있음 · [x] 대결 결과 후 표정이 5-8 표와 일치 · [x] 결과 전 그림에 승패 암시 없음
- [x] 프롬프트에 고정 외형·금지 구절 · [x] 생물 앵커가 아니므로 초파리 해부·현미경 소품 없음 · [x] P1 1장

## 8. 외부 의뢰 묶음
### 의뢰 1/1 · `bg_{key}`
- 올릴 참고 이미지: 없음 · 크기 1920×720 이상 · 받을 파일 이름 `bg_{key}.png`
- 프롬프트: 3-1 그대로 · 네거티브: `blurry, smooth vector art, 3D render, photorealistic, text, letters, numbers, watermark, currency symbol`
- 확인할 것: 왼쪽 45%가 복잡하면 다시, 글자·기호가 생기면 다시

## 7. 매니페스트
```json
{json.dumps({"page": f"{num}_{slug}", "anchor": anc, "season": "default", "duel": {"result": res},
  "images": [{"key": f"bg_{key}", "plate": "F", "size": [1920, 720], "maker": "external", "tool": "genspark", "status": "requested", "priority": "P1", "slot": "hero-bg", "fallback": "pixel-code", "alt": alt_bg},
             {"key": f"sc_{key}_outro", "plate": "E", "size": [1200, 800], "maker": "claude", "status": "placed", "next": "external-optional", "priority": "P2", "slot": "outro", "fallback": "composite"},
             {"key": f"thumb_{key}", "plate": "I", "size": [600, 400], "maker": "claude", "status": "placed", "priority": "P2"},
             {"key": f"og_{key}", "plate": "K", "size": [1200, 630], "maker": "claude", "status": "placed", "priority": "P3"}] +
            [{"key": k, "pack": k, "status": "pack"} for k in packs],
  "character_pack": {"repo": "adminmrobo/fruitfly-lab-expressions", "commit": "ea5da3f"}}, ensure_ascii=False, indent=1)}
```
"""
    open(os.path.join(ROOT, 'docs', f'IMG_{num}_{slug}.md'), 'w').write(md)
    manifest_all.append((num, slug, anc, place_ko))
# chapter index spec
idx = """# 블록체인 2장 공용 이미지 명세서 (`IMG_2-00_index.md`)

| 항목 | 내용 |
|---|---|
| 챕터 | 블록체인 편 2장 「블록체인 기술」, 페이지 7개 + 목차 |
| 시즌 | 기본 |
| 공용 표정 | 캐릭터 팩 (커밋 ea5da3f), `assets/sprites.js`에 96px + 192px 묶음 · 그림 없음 역할 키: doc_scale, asst_ledger, asst_board |

## 1. 목차·표지 그림
| 키 | 판 | 내용 | 제작 | 우선 |
|---|---|---|---|---|
| bg_ch2_index | F | 장부의 부품을 한 장면에: 왼쪽은 단순, 오른쪽으로 갈수록 쪽지 상자 → 지문 카드 → 사슬로 이은 장부 쪽 → 영수증 두루마리 → 생선 상자 꼬리표 → 채굴 장비 → 모래시계가 차례로 놓인 긴 작업실 | 외부 | P1 |
| cover_ch2 | J | 넷이 함께: 박사가 가운데에서 사슬로 이어진 장부 쪽(글자 없음)을 가리키고, 초파리와 Money-Robo가 양쪽에서 올려다보고, 하루가 점수판(빈칸 셋)을 든다 | 외부 | P2 |
| thumb_2_01 ~ thumb_2_07 | I | 각 편 bg를 3:2로 자르기 | 직접 | P2 |

```
""" + f"{STYLE}, wide 8:3 background, left side simple and calm for title text, details on the right, a long workshop beside the lab where objects are lined up from left to right like stages: a crate of bundled paper slips, a fingerprint card under a magnifying glass, blank ledger pages linked by brass chain, a long receipt paper roll, a fish crate with a blank tag, a glowing cyan mining machine, and finally a large brass hourglass, warm golden lamp light growing brighter toward the right, no characters, {NEG}" + """
```

## 2. 페이지별 대표 그림
| 페이지 | 앵커 | bg | outro | 상태 |
|---|---|---|---|---|
""" + '\n'.join(f"| {n} | {a} | bg_{n.replace('-','_')} | sc_{n.replace('-','_')}_outro | bg 의뢰 · outro 합성본 |" for n, s, a, p in manifest_all) + """

## 3. 새 표정 후보 (시리즈 공용, P2)
| 키 | 대신 쓰는 그림 | 쓰는 곳 | 메모 |
|---|---|---|---|
| doc_scale | doc_e13 | 무승부 판정 (2장에는 무승부 없음) | 수평 놋쇠 저울을 두 손으로. 저장소 E25 후보 |
| asst_ledger | asst_e07 | 모든 편 꾸러미 섹션 | 줄무늬 장부를 펼치고 펜 |

## 4. 의뢰 순서 (Genspark 한 세션)
bg_ch2_index → bg_2_01 … bg_2_07 → (선택) cover_ch2 → (선택) sc_2_0n_outro
"""
open(os.path.join(ROOT, 'docs', 'IMG_2-00_index.md'), 'w').write(idx)
# registry: 1장 등록부를 읽고 2장을 합친다
prev = json.load(open('/home/claude/ch1/docs/KG_00_registry.json'))
reg = {"registry": "KG_00_registry", "series": "연구실 해설 대시보드 · 블록체인 편", "chapter": "1–2", "version": "0.2", "updated": "2026-10-29",
       "note": "1장 등록부(v0.1)에 2장을 합친 판. 3장 작업 때 이 파일을 먼저 읽고 같은 개념은 같은 ID를 쓴다. pages에 그 ID를 쓴 편 번호가 모두 적혀 있다.",
       "concepts": prev['concepts'], "works": prev['works'], "conflicts": []}
for f in sorted(os.listdir(SRC)):
    if f.startswith('kg_2-'):
        g = json.load(open(os.path.join(SRC, f)))
        for n in g['nodes']:
            if n['type'] in ('QuizItem', 'Simulation', 'Claim', 'Question'): continue
            box = reg['works' if n['type'] == 'Work' else 'concepts']
            pg = g['page'].split('_')[0]
            if n['id'] in box:
                e = box[n['id']]
                if e['label']['ko'] != n['label']['ko'] or e['type'] != n['type']:
                    reg['conflicts'].append({"id": n['id'], "registry": e['label']['ko'] + ' / ' + e['type'], "page": pg, "label": n['label']['ko'] + ' / ' + n['type']})
            else:
                e = box[n['id']] = {"type": n['type'], "label": n['label'], "pages": []}
            if pg not in e['pages']: e['pages'].append(pg)
json.dump(reg, open(os.path.join(ROOT, 'docs', 'KG_00_registry.json'), 'w'), ensure_ascii=False, indent=1)
print('docs ok', len(reg['concepts']), 'concepts', len(reg['conflicts']), 'conflicts')
for c in reg['conflicts']: print(c)
