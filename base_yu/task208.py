# best: 199(jailctf merger) / others: 223(jacekw Potatoman nauti natte), 223(import itertools), 225(ox jam), 229(jonas ryno kg583 kabutack), 229(JRKX)
def p(g):
 for c in range(1,10):
  a=[(i,j)for i in range(21)for j in range(21)if g[i][j]==c]
  if 0<len(a)<25:
   u,l=min(a)
   d,r=max(a)
   for y in range(21-d+u):
    for x in range(21-r+l):
      for i,j in a*(1-any(g[y+i][x+j]for i in range(1,d-u)for j in range(1,r-l))):
       g[y+i-u][x+j-l]=c
 return g

# def p(g):
#  c=min(sum(g,[]),key=sum(g,[]).count)
#  a=sorted([((r-l)*(d-u),g[u-1][l-1]==c,-l,r,u,d)for r in range(22)for d in range(22)for l in range(r)for u in range(d)if not any(any(s[l:r])for s in g[u:d])])
#  while not a[-1][1]:a.pop()
#  _,_,l,r,u,d=a[-2]
#  g[u-1][~l:r+1]=g[d][~l:r+1]=[c]*(r+l+2)
#  for s in g[u:d]:s[~l]=s[r]=c
#  return g
