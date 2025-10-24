def p(a):
 t=[n[:]for n in a];g,u=len(a),len(a[0])
 for n in range(g):
  for f in range(u):
   if a[n][f]==3:
    for(i,d)in[(0,1),(1,0),(0,-1),(-1,0)]:
     if 0<=n+i<g and 0<=f+d<u and a[n+i][f+d]==3:t[n][f]=8;break
 return t