def p(t,u=range):
 H,W=len(t),len(t[0]);q=min(set(sum(t,[]))-{0,2})
 for f in u(H-1):
  for a in u(W-1):
   d=[t[f+y][a+x]for y,x in zip((0,0,1,1),(0,1,0,1))]
   if all(d):
    for idx,v in enumerate(d):
     if v==2:
      for k in u(10):
       for dy,dx in[(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
        y=f+[-k,k+1][idx>1]+dy;x=a+[-k,k+1][idx%2]+dx
        if 0<=y<H and 0<=x<W:t[y][x]=q
 return t