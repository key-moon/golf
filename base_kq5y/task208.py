# best: 215(jailctf merger) / others: 225(ox jam), 225(xsot ovs att joking mewheni), 229(jonas ryno kg583 kabutack), 229(jonas ryno kg583), 244(jacekwl Potatoman nauti)

# 上の方が圧縮され力が高い そもそもロジックが違う説

def p(s):
 t=sum(s,[])
 g=min(t,key=t.count)
 i=[(c,r)for c in range(21)for r in range(21)if s[c][r]==g]
 f=min(c for c,r in i)
 h=min(r for c,r in i)
 a=max(c for c,r in i)-f+1
 o=max(r for c,r in i)-h+1
 i={(c-f,r-h)for c,r in i}
 for c in range(22-a):
  for r in range(22-o):
   if c^f|r^h and not any(s[c+n][r+e]for n in range(a)for e in range(o)if(n,e)not in i):
    for n,e in i:s[c+n][r+e]=g
    return s

# def p(g):
#  h,w=len(g),len(g[0]);f=sum(g,[]);v=min(f,key=f.count)
#  P=[(r,c)for r in range(h)for c in range(w)if g[r][c]==v]
#  Y,X=zip(*P);a,b=min(Y),min(X);d,e=max(Y)-a+1,max(X)-b+1
#  s={(y-a,x-b)for y,x in P}
#  for y in range(h-d+1):
#   for x in range(w-e+1):
#    if(y,x)!=(a,b)and not any(g[y+k][x+l]for k,l in({(k,l)for k in range(d)for l in range(e)}-s)):
#     for k,l in s:g[y+k][x+l]=v
#     return g
