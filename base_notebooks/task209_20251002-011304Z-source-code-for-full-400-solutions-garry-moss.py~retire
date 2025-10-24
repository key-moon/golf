from itertools import product as P, groupby as f
def p(b):
 R,l=len(b),len(b[0])
 e=sorted((d,x)for d,x in P(range(R),range(l))if b[d][x]==4)
 if len(e)!=4:return[]
 y1,x1,y2,x2=e[0]+e[3]
 n=[(d,x)for d,x in P(range(R),range(l))if b[d][x]and not(y1<=d<=y2 and x1<=x<=x2)]
 if not n:return[[4 if(d,x)in((0,0),(0,x2-x1),(y2-y1,0),(y2-y1,x2-x1))else 0 for x in range(x2-x1+1)]for d in range(y2-y1+1)]
 t,mc=min(d for d,_ in n),min(x for _,x in n)
 B=[(d,x)for d in range(y1,y2+1)for x in range(x1,x2+1)if b[d][x]not in(0,4)]
 if not B:
  r=[[0]*(x2-x1+1)for _ in range(y2-y1+1)]
  r[0][0]=r[0][-1]=r[-1][0]=r[-1][-1]=4
  return r
 def a(b,y1,y2,x1,x2):
  l=float('inf')
  for g in range(y1,y2+1):
   a=[b[g][u]for u in range(x1,x2+1)if b[g][u]not in(0,4)]
   if a:l=min(l,max(sum(1for _ in g)for _,g in f(a)))
  for u in range(x1,x2+1):
   a=[b[g][u]for g in range(y1,y2+1)if b[g][u]not in(0,4)]
   if a:l=min(l,max(sum(1for _ in g)for _,g in f(a)))
  return l if l!=float('inf')else 1
 l=a(b,y1,y2,x1,x2)
 M={}
 for d,x in B:
  p=b[d][x]
  if p not in M:M[p]=[[b[d+g][x+u]for u in range(l)]for g in range(l)]
 o=B[0];fn=b[o[0]][o[1]]
 m=next(((d-t,x-mc)for d,x in n if b[d][x]==fn),(-1,-1))
 def c(yo,o):
  r=[[0]*(x2-x1+1)for _ in range(y2-y1+1)]
  r[0][0]=r[0][-1]=r[-1][0]=r[-1][-1]=4
  for d,x in n:
   m=M.get(b[d][x],[[b[d][x]]*l]*l)
   x,e=yo+(d-t)*l,o+(x-mc)*l
   for q,y in P(range(l),repeat=2):
    d,s=x+q,e+y
    if 0<=d<len(r)and 0<=s<len(r[0]):r[d][s]=m[q][y]
  return r
 yo=(o[0]-y1)-m[0]*l if m!=(-1,-1)else 0
 o=(o[1]-x1)-m[1]*l if m!=(-1,-1)else 0
 r=c(yo,o)
 if any(b[d][x]not in(0,4)and not r[d-y1][x-x1]for d,x in P(range(y1,y2+1),range(x1,x2+1))):
  rb,z,nb=next((d,x,b[d][x])for d in range(y2,y1-1,-1)for x in range(x1,x2+1)if b[d][x]not in(0,4))
  T=[(d,x)for d,x in n if b[d][x]==nb]
  i,mx=max(d for d,_ in T),min(x for _,x in T)
  yo=(rb-y1)-((i-t)*l+l-1)
  o=(z-x1)-(mx-mc)*l
  r=c(yo,o)
 return r