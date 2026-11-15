"""Write `moves`/`move` into entries. Usage: python apply_moves.py data.py  (data.py defines M = {id: (codes, en, zh)})"""
import glob, re, subprocess, sys, json
M = {}
exec(open(sys.argv[1]).read())
paths = {re.search(r'^id: (AWF-\d+)', open(p).read(), re.M).group(1): p for p in glob.glob('workflows/**/README.md', recursive=True) if open(p).read().startswith('---')}
for i, (codes, en, zh) in M.items():
    p = paths['AWF-' + i]
    for path, add in ((p, f"moves: [{', '.join(codes)}]\nmove: {json.dumps(en, ensure_ascii=False)}\n"), (p.replace('README.md', 'README.zh-CN.md'), f"move: {json.dumps(zh, ensure_ascii=False)}\n")):
        t = open(path).read(); head, sep, rest = t[4:].partition('\n---\n')
        assert sep and '\nmove:' not in '\n' + head, path
        if path.endswith('zh-CN.md'):
            head = re.sub(r'(?m)^(source_hash:)', add + r'\1', head, count=1)
        else:
            head = head + '\n' + add.rstrip('\n')
        open(path, 'w').write('---\n' + head + '\n---\n' + rest)
    r = subprocess.run([sys.executable, 'scripts/i18n.py', 'stamp', 'AWF-' + i], capture_output=True, text=True)
    if r.returncode: print('STAMP', i, r.stdout[-300:], r.stderr[-300:])
print(len(M), 'entries')
