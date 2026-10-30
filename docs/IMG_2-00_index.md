# 블록체인 2장 공용 이미지 명세서 (`IMG_2-00_index.md`)

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
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a long workshop beside the lab where objects are lined up from left to right like stages: a crate of bundled paper slips, a fingerprint card under a magnifying glass, blank ledger pages linked by brass chain, a long receipt paper roll, a fish crate with a blank tag, a glowing cyan mining machine, and finally a large brass hourglass, warm golden lamp light growing brighter toward the right, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 2. 페이지별 대표 그림
| 페이지 | 앵커 | bg | outro | 상태 |
|---|---|---|---|---|
| 2-01 | C | bg_2_01 | sc_2_01_outro | bg 의뢰 · outro 합성본 |
| 2-02 | D | bg_2_02 | sc_2_02_outro | bg 의뢰 · outro 합성본 |
| 2-03 | C | bg_2_03 | sc_2_03_outro | bg 의뢰 · outro 합성본 |
| 2-04 | D | bg_2_04 | sc_2_04_outro | bg 의뢰 · outro 합성본 |
| 2-05 | D | bg_2_05 | sc_2_05_outro | bg 의뢰 · outro 합성본 |
| 2-06 | C | bg_2_06 | sc_2_06_outro | bg 의뢰 · outro 합성본 |
| 2-07 | C | bg_2_07 | sc_2_07_outro | bg 의뢰 · outro 합성본 |

## 3. 새 표정 후보 (시리즈 공용, P2)
| 키 | 대신 쓰는 그림 | 쓰는 곳 | 메모 |
|---|---|---|---|
| doc_scale | doc_e13 | 무승부 판정 (2장에는 무승부 없음) | 수평 놋쇠 저울을 두 손으로. 저장소 E25 후보 |
| asst_ledger | asst_e07 | 모든 편 꾸러미 섹션 | 줄무늬 장부를 펼치고 펜 |

## 4. 의뢰 순서 (Genspark 한 세션)
bg_ch2_index → bg_2_01 … bg_2_07 → (선택) cover_ch2 → (선택) sc_2_0n_outro
