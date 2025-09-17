# best: 208(xsot ovs att joking mewheni) / others: 217(jailctf merger), 218(4atj sisyphus luke Seek mukundan), 255(natte), 280(MasukenSamba), 307(jonas ryno kg583)
def p(g):
 t=sum(g,[])
 u,l=divmod(t.index(4),13)
 d,r=divmod(168-t[::-1].index(4),13)
 m=[]
 for s in g[u:d+1]:
  m+=s[l:r+1],
  s[l:r+1]=[0]*(r-l+1)
 w=[[v for*s,v in zip(*g,s)if any(s)] for s in g if any(s)]
 f=[*map(max,*w)][0]!=m[1][0]
 return m[:1]+[[y[0],*x[::1|-f],y[-1]] for x,y in zip(w,m[1:])]+m[-1:]
