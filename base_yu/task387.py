#上下の囲み+左右方向の破線を書く→90度回転
R=range
def p(g):
 h,w=len(g),len(g[0])
 u=[s[:]for s in g]
 for _ in 0,1:
  for i in R(h):
   if a:=[j for j in R(w)if (s:=g[i])[j]]:
    j,k=a
    l,r=u[i-1],u[i+1]
    l[j-1:j+2]=r[j-1:j+2]=[s[k]]*3
    l[k-1:k+2]=r[k-1:k+2]=[s[j]]*3
    for t in R(j+2,k-1):
     u[i][t]=-~min(t-j,k-t)%2*5
  *g,=zip(*g)
  *u,=map(list,zip(*u))
  h,w=w,h
 return u
