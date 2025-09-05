# best: 57(sisyphus) / others: 58(luke), 58(att), 64(Bulmenisaurus), 64(biz), 64(4atj)
# lambda g:[[g[i//2|1][j//2|1] for j in range(len(g[0])*2)] for i in range(len(g)*2)]
# lambda g:sum([[[int,p][r*0!=0](r)]*4for r in g[1::2]],[])
# ========================== 57 =========================
p=lambda g:g*0!=0and sum([[p(r)]*4for r in g[1::2]],[])or g
