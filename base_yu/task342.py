# best: 111(jailctf merger) / others: 112(4atj sisyphus luke Seek mukundan), 119(xsot ovs att joking mewheni), 129(natte), 136(dbdr), 138(MasukenSamba)
# ==================================================== 111 ====================================================
def p(g):
 i=sum(g,[]).index(8)//10
 *x,=filter(int,sum([*zip(*g[:i]),*zip(*g[i+2:])],()))
 return[[v==8 and x.pop(0)for v in s]for s in g]








