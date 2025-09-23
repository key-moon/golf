# best: 105(ox jam, 4atj sisyphus luke Seek mukundan, intgrah jimboko awu macaque sammyuri) / others: 106(Yuchen20), 107(natte), 108(JRKX), 108(jonas ryno kg583 kabutack), 108(jonas ryno kg583)
# ================================================= 105 =================================================
# lambda g,c=-1:c*[[x&y for x in s[::3]for y in t[::3]]for s in g[::3]for t in g[::3]]or[*zip(*filter(max,p(g,c+1)))]
p=lambda g,c=-1:c*[[x&y for x in s for y in t]for s in g for t in g]or p([*zip(*filter(max,g[::3]))],c+1)
