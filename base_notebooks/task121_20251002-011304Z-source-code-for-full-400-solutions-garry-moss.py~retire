def p(i):
 for u in range(1,len(i)-1):
  for r in range(1,len(i[0])-1):
   if i[u][r]==8:
    n=[]
    for o in[-1,0,1]:
     for b in[-1,0,1]:
      if(o or i)and i[u+o][r+b]:n.append(i[u+o][r+b])
    t=max(set(n),key=n.count);i=[[i[u+n][r+o]for o in[-1,0,1]]for n in[-1,0,1]];i[1][1]=t;return i