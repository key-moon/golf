# best: 199(jailctf merger) / others: 208(ox jam), 218(Code Golf International), 218(4atj sisyphus luke Seek mukundan), 230(import itertools), 235(intgrah jimboko awu macaque sammyuri)
# def p(g):
#  t=sum(g,[])
#  u,l=divmod(t.index(4),13)
#  d,r=divmod(168-t[::-1].index(4),13)
#  m=[]
#  for s in g[u:d+1]:
#   m+=s[l:r+1],
#   s[l:r+1]=[0]*(r-l+1)
#  w=[[v for*s,v in zip(*g,s)if any(s)] for s in g if any(s)]
#  f=[*map(max,*w)][0]!=m[1][0]
#  return m[:1]+[[y[0],*x[::1|-f],y[-1]] for x,y in zip(w,m[1:])]+m[-1:]

def p(g):
 *g,=map(list,zip(*g))
 k=sum(g,[]).index(4)
 l=g[k//13][k%13+1:].index(4)+2
 a=g[k//13][k%13:k%13+l]
 g[k//13][k%13:k%13+l]=[0]*l
 k=sum(g,[]).index(4)
 l=g[k//13][k%13+1:].index(4)+2
 b=g[k//13][k%13:k%13+l]
 g[k//13][k%13:k%13+l]=[0]*l
 *g,=filter(any,zip(*g))
 *g,=filter(any,zip(*g))
 return [*zip(a,*[[0,*s,0]for s in g][::1|-(max(g[0])!=a[1])],b)]
