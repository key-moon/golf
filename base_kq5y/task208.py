# best: 215(jailctf merger) / others: 225(xsot ovs att joking mewheni), 249(4atj sisyphus luke Seek mukundan), 249(mukundan), 294(Jonas), 294(kdmitrie)

# 上の方が圧縮され力が高い そもそもロジックが違う説

def p(g):
 F=sum(g,[])
 C=min(F,key=F.count)
 S=[(r,c)for r in range(21)for c in range(21)if g[r][c]==C]
 a=min(r for r,c in S)
 b=min(c for r,c in S)
 d=max(r for r,c in S)-a+1
 e=max(c for r,c in S)-b+1
 S={(r-a,c-b)for r,c in S}
 for r in range(22-d):
  for c in range(22-e):
   if r^a|c^b and not any(g[r+h][c+i]for h in range(d)for i in range(e)if(h,i)not in S):
    for h,i in S:g[r+h][c+i]=C
    return g

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
