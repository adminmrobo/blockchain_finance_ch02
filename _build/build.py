import importlib, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pages'))
from template import page
from common import build
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
CHAPTER = {'title': '2장 「블록체인 기술」', 'short': '블록체인 2장', 'eyebrow': '연구실 해설 대시보드 · 블록체인 편 2장 「블록체인 기술」',
  'next_chapter': '3장 「비트코인」 (다음 저장소)', 'prev_chapter': '1장 「장부의 진화」 (이전 저장소)',
  'pages': [{'num': '2-01', 'file': '2-01_block-bundle.html', 'short': '블록: 묶음 단위'},
            {'num': '2-02', 'file': '2-02_hash-fingerprint.html', 'short': '해시: 데이터의 지문'},
            {'num': '2-03', 'file': '2-03_hash-chain.html', 'short': '해시 사슬'},
            {'num': '2-04', 'file': '2-04_history-not-database.html', 'short': 'DB가 아닌 이력'},
            {'num': '2-05', 'file': '2-05_provenance-cases.html', 'short': '이력 관리 사례'},
            {'num': '2-06', 'file': '2-06_mining-race.html', 'short': '채굴 경주'},
            {'num': '2-07', 'file': '2-07_difficulty-and-confirmation.html', 'short': '난이도와 확정'}]}
which = sys.argv[1:] or ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
built = []
for mname in which:
    if not os.path.exists(os.path.join(SRC, 'pages', mname + '.py')): continue
    m = importlib.import_module(mname); P = m.PAGE
    P['js'] = open(os.path.join(SRC, 'pages', mname + '.js')).read()
    n, e = build(P, P['num'], P['slug'])
    fn = f"{P['num']}_{P['slug']}.html"
    open(os.path.join(ROOT, fn), 'w').write(page(P, CHAPTER))
    built.append((fn, n, e)); json.dump(P['kg'], open(os.path.join(SRC, f"kg_{P['num']}.json"), 'w'), ensure_ascii=False)
    json.dump({'num': P['num'], 'title': P['meta_title'], 'anchor': P['anchor'], 'key': P['key'], 'duel': P['duel']['title']}, open(os.path.join(SRC, f"info_{P['num']}.json"), 'w'), ensure_ascii=False)
for b in built: print(*b)
# CSS
open(os.path.join(ROOT, 'assets', 'lab.css'), 'w').write(open(os.path.join(SRC, 'base.css')).read() + open(os.path.join(SRC, 'extra.css')).read())
open(os.path.join(ROOT, 'assets', 'lab.js'), 'w').write(open(os.path.join(SRC, 'lab.js')).read())
# sprites: collect keys from all html
keys = set()
for f in os.listdir(ROOT):
    if f.endswith('.html'):
        keys |= set(re.findall(r'data-img="((?:doc|asst|fly|robo)_e\d\d)"', open(os.path.join(ROOT, f)).read()))
roles = 'fly_point,fly_arms,fly_coffee,fly_cry,robo_coin,robo_happy,robo_sigh,robo_meh,robo_blush,asst_firm,asst_spark,asst_shock,asst_smile,doc_judge,doc_scale,asst_ledger'
pick = ','.join(sorted(keys)) + ',' + roles
pack = '/home/claude/pack/character_pack'
o96 = subprocess.run(['python3', 'build_character_pack.py', '--pack', '.', '--size', '96', '--pick', pick], cwd=pack, capture_output=True, text=True).stdout
stage = set()
for f in os.listdir(ROOT):
    if f.endswith('.html'):
        for blk in re.findall(r'<div class="stage".*?</div>', open(os.path.join(ROOT, f)).read(), re.S): stage |= set(re.findall(r'data-img="(\w+_e\d\d)"', blk))
o192 = subprocess.run(['python3', 'build_character_pack.py', '--pack', '.', '--size', '192', '--pick', 'fly_point,fly_arms,fly_coffee,fly_cry,robo_coin,robo_happy,robo_sigh,robo_meh,robo_blush,' + ','.join(sorted(stage))], cwd=pack, capture_output=True, text=True).stdout
s192 = re.search(r'var SPRITE=(\{.*?\});', o192, re.S).group(1)
open(os.path.join(ROOT, 'assets', 'sprites.js'), 'w').write(o96 + '\nvar SPRITE192=' + s192 + ';\n')
print('sprites KB', os.path.getsize(os.path.join(ROOT, 'assets', 'sprites.js')) // 1024)
