# best: 112(4atj sisyphus luke Seek mukundan) / others: 117(jailctf merger), 119(xsot ovs att joking mewheni), 129(natte), 136(dbdr), 138(MasukenSamba)
# ==================================================== 112 =====================================================
def p(g):
 i=sum(g,[]).index(8)//10
 *x,=filter(int,sum([*zip(*g[:i]),*zip(*g[i+2:])],()))
 return[[v==8 and x.pop(0)for v in s]for s in g]


