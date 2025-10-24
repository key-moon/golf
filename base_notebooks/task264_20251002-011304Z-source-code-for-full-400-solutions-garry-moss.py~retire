j=len
a=range
n=[1,4,9,16,25,36,49,64,81]
s=[-1,0,1]
x=[[f,n]for f in s for n in s]
e=[264,246,236,194,285,134,156,66,104]
def p(h):
 d,u=j(h),j(h[0]);f=[[0]*9for f in a(9)]
 for d in a(1,d-1):
  for l in a(1,u-1):
   g=[h[d+f][l+n]for(f,n)in x];t=sum([n[f]for f in a(9)if g[f]==5])
   if t in e and 0not in g:
    g=e.index(t)
    for s in a(3):
     for k in a(3):f[s+g//3*3][k+g%3*3]=h[d-1+s][l-1+k]
 return f