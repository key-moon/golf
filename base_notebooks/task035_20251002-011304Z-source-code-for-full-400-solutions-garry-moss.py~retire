h=len
b=range
r=[[0,1],[0,-1],[1,0],[-1,0]]
def p(a):
 c,c=h(a),h(a[0])
 for t in b(c):
  for o in b(c):
   if a[t][o]==8:
    for(p,u)in r:
     if a[t+p][o+u]==0:
      for d in b(20):
       if 0<=t+p*d<c and 0<=o+u*d<c:
        l=a[t+p*d][o+u*d]
        if l>0:a[t][o]=l
 return a