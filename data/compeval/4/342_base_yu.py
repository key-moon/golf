# best: 112(mukundan) / others: 119(joking), 119(joking MeWhenI), 129(natte), 132(4atj sisyphus luke Seek), 136(dbdr)
# ==================================================== 112 =====================================================
def p(g):
 i=sum(g,[]).index(8)//10
 *x,=filter(int,sum([*zip(*g[:i]),*zip(*g[i+2:])],()))
 return[[v==8 and x.pop(0)for v in s]for s in g]
