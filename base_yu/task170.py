# best: 163(jailctf merger) / others: 166(Code Golf International), 170(FuunAgent), 180(import itertools), 191(LogicLynx), 193(lv1.dev)
# ============================================================================== 163 ==============================================================================
def p(g):
 y,x,c=zip(*[(i,j,v)for i,s in enumerate(g)for j,v in enumerate(s)if v])
 d=3+1%len({*c[:-9]})
 R=range(d)
 k=-d*d
 l=(y[k-1]-y[0]+1)//d
 return[[g[i*l+y[0]][j*l+min(x[:k])]and g[y[k]+i][x[k]+j]for j in R]for i in R]
