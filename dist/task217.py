E=lambda g:filter(max,zip(*g))
p=lambda g:[[x&y for x in s for y in t]for s in E(E(g))for t in E(E(g))]