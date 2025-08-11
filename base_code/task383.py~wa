def p(g):
 h,w=len(g),len(g[0]);d={}
 for r in g:
  for v in r:
   if v:d[v]=d.get(v,0)+1
 k=sorted(d,key=d.get);F,I=k[-1],k[-2]
 for y in range(h):
  for x in range(w):
   if g[y][x]==I:
    c=0
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     try:
      if g[y+dy][x+dx]==I:c+=1
     except:pass
    if c-1:continue
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
     s=1
     while 1:
      try:w=g[y+dy*s][x+dx*s]
      except:break
      if w==F:s+=1
      elif w==0:g[y+dy*s][x+dx*s]=I;s+=1
      else:break
 return g
