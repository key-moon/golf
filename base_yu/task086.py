# best: 172(ox jam) / others: 176(jailctf merger), 179(4atj sisyphus luke Seek mukundan), 233(intgrah jimboko awu macaque sammyuri), 242(natte), 256(kdmitrie)
# ================================================================================== 172 ===================================================================================

# ↓このコードは [Yuくんのcommit](https://github.com/key-moon/golf/commit/11125032033087d2f61e09dcacaf810a6c1e4a0d) のもの
# 変数名置換くんとの相性が悪くてなんか死んでるっぽいので一旦コメントアウトします、解決したら戻したい（Yuくんごめん）
import re
def p(g):
 C,D,_=sorted({*sum(g,[])},key=sum(g,[]).count)
 g=eval(re.sub("(?=[1-9])",r"C^D^",str(g)))
 g=[*zip(*eval(re.sub("0(?=(, %d|(, 0)?, %d, .), ., %d)"%(C,C,C),str(D),str(g)))[::-1])]
 g=[*zip(*eval(re.sub("0(?=(, %d|(, 0)?, %d, .), ., %d)"%(C,C,C),str(D),str(g)))[::-1])]
 g=[*zip(*eval(re.sub("0(?=(, %d|(, 0)?, %d, .), ., %d)"%(C,C,C),str(D),str(g)))[::-1])]
 g=[*zip(*eval(re.sub("0(?=(, %d|(, 0)?, %d, .), ., %d)"%(C,C,C),str(D),str(g)))[::-1])]
 return g

# def p(g):
#  c,d,_=sorted({*sum(g,[])},key=sum(g,[]).count)
#  u=[s[:]for s in g]
#  for i in range(len(g)):
#   for j in range(len(g[0])):
#    for k in range(4):
#     if any(all(len(g)>i+~-abs(k-1)*t>-1<j+~-abs(k-2)*t<len(g[0])and d==g[i+~-abs(k-1)*t][j+~-abs(k-2)*t]for t in[s//2+1,s+3])for s in range(3)):
#     # if any(all(len(g)>i+~-abs(k-1)*t>-1<j+~-abs(k-2)*t<len(g[0])and d==g[i+~-abs(k-1)*t][j+~-abs(k-2)*t]for t in s)for s in((1,3),(1,4),(2,5))):
#      u[i][j]=d
#    if g[i][j]:
#     u[i][j]=g[i][j]^c^d
#  return u

# def p(g):
#  G=sum(g,[])
#  c,d,_=sorted({*G},key=G.count)
#  u=[s[:]for s in g]
#  h,w=len(g),len(g[0])
#  for i in range(h):
#   for j in range(w):
#    if g[i][j]:
#     u[i][j]=g[i][j]^c^d
#    else:
#     for k in range(4):
#      for s,t in ((1,3),(1,4),(2,5)):
#       y=i+~-abs(k-1)*s
#       x=j+~-abs(k-2)*s
#       Y=i+~-abs(k-1)*t
#       X=j+~-abs(k-2)*t
#       if h>y>-1<x<w and h>Y>-1<X<w and g[y][x]==g[Y][X]==d:
#        u[i][j]=d
#  return u
