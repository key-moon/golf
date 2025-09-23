def p(g):
 r=[f[:]for f in g];k={(x,a)for x in range(len(g))for a in range(len(g[0]))if g[x][a]==1}
 if not k:return r
 for o in[0,1]:
  l=set()
  for x,a in k:
   for x,a in[(5-x+o,a-5),(5-a+o,4-x+o),(x-5,a-4)]:
    if -5<=x<=5 and -5<=a<=5:l.add((x,a))
  p=[r for r in l if all((5-x+o,5+a)in k or not(0<=5-x+o<len(g)and 0<=5+a<len(g[0]))for x,a in[r])and all((4-a+o,5-x+o)in k or not(0<=4-a+o<len(g)and 0<=5-x+o<len(g[0]))for x,a in[r])and all((5+a,4+x)in k or not(0<=5+a<len(g)and 0<=4+x<len(g[0]))for x,a in[r])and any(0<=5-x+o<len(g)and 0<=5+a<len(g[0])and(5-x+o,5+a)in k for x,a in[r])]
  if p:
   s={(5-x+o,5+a)for x,a in p if 0<=5-x+o<len(g)and 0<=5+a<len(g[0])}|{(4-a+o,5-x+o)for x,a in p if 0<=4-a+o<len(g)and 0<=5-x+o<len(g[0])}|{(5+a,4+x)for x,a in p if 0<=5+a<len(g)and 0<=4+x<len(g[0])}
   if s==k:
    for x,a in p:
     if 0<=4+x<len(r)and 0<=4-a+o<len(r[0])and r[4+x][4-a+o]==0:r[4+x][4-a+o]=2
    break
 return r