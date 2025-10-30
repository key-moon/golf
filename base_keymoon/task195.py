# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, HIMAGINE THE FUTURE., ox jam, biz) / others: 106(jacekw Potatoman nauti natte), 106(import itertools), 106(jailctf merger), 106(Yuchen20), 107(natte)
# ================================================= 105 =================================================
# lambda g,c=-1:c*[[x&y for x in s[::3]for y in t[::3]]for s in g[::3]for t in g[::3]]or[*zip(*filter(max,p(g,c+1)))]
p=lambda g,c=-1:c*[[x&y for x in s for y in t]for s in g for t in g]or p([*zip(*filter(max,g[::3]))],c+1)
