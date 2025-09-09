# best: 194(4atj sisyphus luke Seek mukundan) / others: 199(jailctf merger), 199(xsot ovs att joking mewheni), 244(kdmitrie), 252(MasukenSamba), 257(jonas ryno kg583)
# ============================================================================================= 194 ==============================================================================================

# def p(a):
#  R=range(10)
#  def f(y,x):
#   if y in R and x in R and a[y][x]==8:a[y][x]=0;return{(y,x)}|f(y+1,x)|f(y-1,x)|f(y,x+1)|f(y,x-1)
#   return set()
#  s=[t for i in range(100)if(t:=f(i//10,i%10))]
#  n=[frozenset((r-min(p[0]for p in t),c-min(p[1]for p in t))for r,c in t)for t in s]
#  for i,t in enumerate(s):
#   for y,x in t:a[y][x]=1+(n.count(n[i])==1)
#  return a

# if 0<=y<10>x>=0 and a[y][x]==8:a[y][x]=0;return {(y,x)}|f(y+1,x)|f(y-1,x)|f(y,x+1)|f(y,x-1)

def p(a):
 def f(y,x):
  if 0<=y<10>x>=0<a[y][x]:a[y][x]=0;return{(y,x)}|f(y+1,x)|f(y-1,x)|f(y,x+1)|f(y,x-1)
  return set()
 s=[t for i in range(99)if(t:=f(i//10,i%10))]
 n=[{(r-min(c[0]for c in t),c-min(c[1]for c in t))for r,c in t}for t in s]
 for i,t in enumerate(s):
  for y,x in t:a[y][x]=1+(n.count(n[i])<2)
 return a



