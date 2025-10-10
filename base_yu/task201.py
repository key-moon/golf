# best: 199(jailctf merger) / others: 208(ox jam), 218(4atj sisyphus luke Seek mukundan), 235(intgrah jimboko awu macaque sammyuri), 237(jacekw Potatoman nauti natte), 237(import itertools)
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
