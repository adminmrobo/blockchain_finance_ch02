# 2-06 「채굴 — 블록을 쓰는 권리와 그 비용」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 2-06_mining-race.html |
| 모드 / 주 앵커 | 교과서 / C 장부: 채굴실: 번호 자물쇠 상자들, 빛나는 채굴 장비, 금화 더미 |
| 시즌 | 기본 |
| 대결 | 장비 1대 vs 4대, 블록 100개 경주 → 결과 **R** (Money-Robo 승) |
| 새로 그릴 그림 | P1 1장 · P2 2장 · P3 1장 |
| 제작 경로 | 직접 3장 (합성본·합성 방법) · 외부 의뢰 1장 (+ 선택 1장) |
| 의뢰 도구 | Genspark (기본) |
| 진행 | 받음 0 / 의뢰 1 · 마지막 반영 아직 |
| 캐릭터 팩 표정 | 16장 + 대결 결과용 역할 키 (팩 커밋 ea5da3f, 공용 assets/sprites.js) |
| 그림이 없을 때 | 페이지는 캐릭터 팩 표정, 픽셀 코드 히어로, CSS 무대로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 · 캐릭터 고정 외형: SKILL 18-4 (공식 저장소 `CHARACTER_CORE_EN`)
- 이 페이지 장소: 채굴실: 번호 자물쇠 상자들, 빛나는 채굴 장비, 금화 더미
- 장소 영어 묘사: *a mining room beside the accounting room, many small locked boxes with combination dials on shelves, glowing cyan mining machines with fans, piles of gold coins being dropped into four separate trays, warm golden lamp light*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 제작 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|---|
| 1 | bg_2_06 | F | 1920×720 | 의뢰 | 외부 | P1 | 히어로 배경 | 픽셀 코드 배경 (금고·금화·로봇) |
| 2 | sc_2_06_outro | E | 1200×800 | 넣음 (합성본) | 직접 → 외부 선택 | P2 | 아웃트로 무대 | 팩 캐릭터 4명 CSS 무대 |
| 3 | thumb_2_06 | I | 600×400 | 넣음 (합성 방법 지정) | 직접 | P2 | 목차 카드 | bg_2_06을 3:2로 자르기 |
| 4 | og_2_06 | K | 1200×630 | 넣음 (합성 방법 지정) | 직접 | P3 | 공유 미리보기 | CSS 배경 + fly_e08·robo_e16 + 제목 |
| 5 | asst_e07 | B | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 6 | asst_e10 | B | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 7 | asst_e12 | B | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 8 | asst_e13 | B | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 9 | asst_e16 | B | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 10 | doc_e07 | A | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 11 | doc_e08 | A | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 12 | doc_e09 | A | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 13 | doc_e10 | A | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 14 | fly_e08 | C | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 15 | fly_e09 | C | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 16 | fly_e10 | C | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 17 | fly_e21 | C | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 18 | robo_e12 | D | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 19 | robo_e13 | D | 팩 96 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |
| 20 | robo_e16 | D | 팩 96·192 | 팩 | — | — | 페이지 안 말풍선·대결·아웃트로 | — |

대결 결과용 표정(fly_arms·fly_coffee·fly_cry·robo_happy·robo_sigh·robo_meh·robo_blush·asst_firm·asst_spark·asst_shock·doc_judge·doc_scale)은 공용 sprites.js에 들어 있다. doc_scale은 그림 없음 → doc_e13 (P2 새 표정 후보, 시리즈 공용 명세서 참고).

## 3. 새로 그릴 그림 상세

### 3-1. `bg_2_06` — 대표 배경
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 |
| 제작 경로 | 외부: Genspark |
| 구도 | 왼쪽 45%는 단순한 어두운 벽·바닥(제목 자리), 오른쪽에 장소 소품 |
| 피할 것 | 글자·숫자·₿·실제 화폐 무늬, 실존 은행·기관 로고, 인물 |
| 대체 글 (alt) | 번호 자물쇠 상자와 빛나는 채굴 장비, 금화 더미가 있는 채굴실 |

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a mining room beside the accounting room, many small locked boxes with combination dials on shelves, glowing cyan mining machines with fans, piles of gold coins being dropped into four separate trays, warm golden lamp light, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-2. `sc_2_06_outro` — 아웃트로 장면 (선택)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 제작 경로 | 지금: 팩 캐릭터 CSS 무대 합성(페이지에 있음) → 외부 의뢰 선택 |
| 구도 | MONEY-ROBO in front raising both arms beside four glowing mining machines and a big coin tray, the Fruit Fly behind with waterfall tears beside a single small machine but nodding in acceptance |
| 대체 글 (alt) | 페이지 `.stage`의 aria-label과 같음 |

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a mining room beside the accounting room, many small locked boxes with combination dials on shelves, glowing cyan mining machines with fans, piles of gold coins being dropped into four separate trays, warm golden lamp light, the Fruit Fly, a tiny expressive cartoon fruit fly researcher with a dark charcoal-black segmented insect body, large glossy red compound eyes, a retro dark blue helmet with a yellow-white center stripe and small round side bolts, colorful dangling cables in magenta, purple and blue curving from the back of the helmet, a tiny white lab coat over a black vest, translucent veined wings, six thin black legs with the front pair used like hands; MONEY-ROBO, a cute small floating chibi robot with a large glossy rounded-square white head and a small rounded white body with thick black outlines, a black pill-shaped screen face showing golden-yellow pixel eyes and mouth, a small round knob antenna on a short stem, stubby rounded fingerless arms, no legs, a black oval chest panel with a bright cyan pill-shaped core light, hovering above a small dark oval shadow; the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks; Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat; composition: MONEY-ROBO in front raising both arms beside four glowing mining machines and a big coin tray, the Fruit Fly behind with waterfall tears beside a single small machine but nodding in acceptance; the winner is in front and larger, the other side shows an accepting gesture, no mocking, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `thumb_2_06`, `og_2_06` — 직접 합성
- thumb: bg_2_06을 받으면 오른쪽 소품 부분을 3:2로 자른다. 받기 전에는 CSS 배경 + 팩 캐릭터 1명.
- og: 배경 + fly_e08(오른쪽 봄)·robo_e16(왼쪽 봄) 192px + 제목 글자(HTML·SVG).

## 4. 일관성 지침
- 참고 이미지: 저장소 `refs/original/keyart_rivals.png` + 장면에 나오는 캐릭터의 원본 표정 PNG
- 같은 챕터 그림은 한 도구·한 세션에서 2-01 → 2-07 순서로 (배경 7장 먼저, 장면은 그다음)
- 투명 배경이 안 되면 *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
SKILL 18-15. `python3 build_character_pack.py --ingest 받은폴더/ --plates bg_2_06=F,sc_2_06_outro=E --out received_2_06` → 결과 조각을 `assets/` 쪽 공용 파일이 아니라 이 페이지 스크립트의 `Object.assign(SPRITE,...)`로 넣는다(배경은 페이지마다 다르므로).

## 6. 체크리스트
- [x] HTML의 모든 `data-img` 키가 이 명세서에 있음 · [x] 대결 결과 후 표정이 5-8 표와 일치 · [x] 결과 전 그림에 승패 암시 없음
- [x] 프롬프트에 고정 외형·금지 구절 · [x] 생물 앵커가 아니므로 초파리 해부·현미경 소품 없음 · [x] P1 1장

## 8. 외부 의뢰 묶음
### 의뢰 1/1 · `bg_2_06`
- 올릴 참고 이미지: 없음 · 크기 1920×720 이상 · 받을 파일 이름 `bg_2_06.png`
- 프롬프트: 3-1 그대로 · 네거티브: `blurry, smooth vector art, 3D render, photorealistic, text, letters, numbers, watermark, currency symbol`
- 확인할 것: 왼쪽 45%가 복잡하면 다시, 글자·기호가 생기면 다시

## 7. 매니페스트
```json
{
 "page": "2-06_mining-race",
 "anchor": "C",
 "season": "default",
 "duel": {
  "result": "R"
 },
 "images": [
  {
   "key": "bg_2_06",
   "plate": "F",
   "size": [
    1920,
    720
   ],
   "maker": "external",
   "tool": "genspark",
   "status": "requested",
   "priority": "P1",
   "slot": "hero-bg",
   "fallback": "pixel-code",
   "alt": "번호 자물쇠 상자와 빛나는 채굴 장비, 금화 더미가 있는 채굴실"
  },
  {
   "key": "sc_2_06_outro",
   "plate": "E",
   "size": [
    1200,
    800
   ],
   "maker": "claude",
   "status": "placed",
   "next": "external-optional",
   "priority": "P2",
   "slot": "outro",
   "fallback": "composite"
  },
  {
   "key": "thumb_2_06",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "maker": "claude",
   "status": "placed",
   "priority": "P2"
  },
  {
   "key": "og_2_06",
   "plate": "K",
   "size": [
    1200,
    630
   ],
   "maker": "claude",
   "status": "placed",
   "priority": "P3"
  },
  {
   "key": "asst_e07",
   "pack": "asst_e07",
   "status": "pack"
  },
  {
   "key": "asst_e10",
   "pack": "asst_e10",
   "status": "pack"
  },
  {
   "key": "asst_e12",
   "pack": "asst_e12",
   "status": "pack"
  },
  {
   "key": "asst_e13",
   "pack": "asst_e13",
   "status": "pack"
  },
  {
   "key": "asst_e16",
   "pack": "asst_e16",
   "status": "pack"
  },
  {
   "key": "doc_e07",
   "pack": "doc_e07",
   "status": "pack"
  },
  {
   "key": "doc_e08",
   "pack": "doc_e08",
   "status": "pack"
  },
  {
   "key": "doc_e09",
   "pack": "doc_e09",
   "status": "pack"
  },
  {
   "key": "doc_e10",
   "pack": "doc_e10",
   "status": "pack"
  },
  {
   "key": "fly_e08",
   "pack": "fly_e08",
   "status": "pack"
  },
  {
   "key": "fly_e09",
   "pack": "fly_e09",
   "status": "pack"
  },
  {
   "key": "fly_e10",
   "pack": "fly_e10",
   "status": "pack"
  },
  {
   "key": "fly_e21",
   "pack": "fly_e21",
   "status": "pack"
  },
  {
   "key": "robo_e12",
   "pack": "robo_e12",
   "status": "pack"
  },
  {
   "key": "robo_e13",
   "pack": "robo_e13",
   "status": "pack"
  },
  {
   "key": "robo_e16",
   "pack": "robo_e16",
   "status": "pack"
  }
 ],
 "character_pack": {
  "repo": "adminmrobo/fruitfly-lab-expressions",
  "commit": "ea5da3f"
 }
}
```
