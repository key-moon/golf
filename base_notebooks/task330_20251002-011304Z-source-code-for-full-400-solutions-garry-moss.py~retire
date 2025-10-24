from collections import Counter,deque
def p(t,l=range):
 h,s=len(t),len(t[0]);p=Counter(r for o in t for r in o).most_common(1)[0][0];k=[o[:]for o in t];g=[[0]*s for o in l(h)]
 for o in l(h):
  for r in l(s):
   if t[o][r]!=p and not g[o][r]:
    q=t[o][r];j=deque([(o,r)]);g[o][r]=1;n=[]
    while j:
     f,i=j.popleft();n.append((f,i))
     for(m,u)in((1,0),(-1,0),(0,1),(0,-1)):
      a,c=f+m,i+u
      if 0<=a<h and 0<=c<s and not g[a][c]and t[a][c]==q:g[a][c]=1;j.append((a,c))
    c=2if len(n)==6else 1
    for(f,i)in n:k[f][i]=c
 return k