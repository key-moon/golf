def p(g):
 a,b=[[i for i,c in enumerate(M)if all(c)]for M in(zip(*g),g)]
 x=[r[a[0]:a[-1]+1]for r in g[b[0]:b[-1]+1]]
 m=max(max(r[1:-1])for r in x[1:-1])
 h=m in(x[1][0],x[1][-1])
 if h:x=[*map(list,zip(*x))]
 t=(x[1:-1],x[-2:0:-1])[m==x[0][1]]
 for j in range(1,len(x[0])-1):
  s=0
  for r in t:s|=r[j]==m;r[j]=r[j]or m*s
 if h:x=[*map(list,zip(*x))]
 return x