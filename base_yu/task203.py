# best: 64(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 67(dbdr), 67(import itertools), 67(Yuchen20), 67(ox jam), 69(2F)
# ============================= 64 =============================
# p=lambda g:(n:=len(g)//2)and[[g[n][g[n].index(v)+n]for v in s]for s in g]
p=lambda g:[[g[n:=len(g)//2][s.index(v)+n]for v in s]for s in g]
