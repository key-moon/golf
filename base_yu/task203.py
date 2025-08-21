# best: 64(Seek64) / others: 67(dbdr), 67(4atj), 67(joking), 68(sisyphus), 69(luke)
# ============================= 64 =============================
# p=lambda g:(n:=len(g)//2)and[[g[n][g[n].index(v)+n]for v in s]for s in g]
p=lambda g:[[g[n:=len(g)//2][g[n].index(v)+n]for v in s]for s in g]