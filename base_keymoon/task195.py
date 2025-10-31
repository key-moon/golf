# best: 94(ox jam) / others: 102(lv1.dev), 103(Code Golf International), 105(4atj sisyphus luke Seek mukundan), 105(FuunAgent), 105(HIMAGINE THE FUTURE.)
# ============================================ 94 ============================================
# lambda g,c=-1:c*[[x&y for x in s[::3]for y in t[::3]]for s in g[::3]for t in g[::3]]or[*zip(*filter(max,p(g,c+1)))]
p=lambda g,c=-1:c*[[x&y for x in s for y in t]for s in g for t in g]or p([*zip(*filter(max,g[::3]))],c+1)
