# best: 64(jailctf merger, 4atj sisyphus luke Seek mukundan) / others: 67(dbdr), 67(Yuchen20), 67(ox jam), 67(import itertools), 69(2F)
# ============================= 64 =============================
# p=lambda g:(n:=len(g)//2)and[[g[n][g[n].index(v)+n]for v in s]for s in g]
p=lambda g:[[g[n:=len(g)//2][s.index(v)+n]for v in s]for s in g]
