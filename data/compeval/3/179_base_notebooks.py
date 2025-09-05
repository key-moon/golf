def p(g):
 h,w=len(g),len(g[0])
 b=[]
 for i in range(0,h,3):
  for j in range(0,w,1):
   for bi in range(3):
    for bj in range(1):
     b.append(g[i+bi][j+bj])
 oh,ow=3,3
 res=[[0]*ow for _ in range(oh)]
 for idx,v in enumerate(b[:oh*ow]):
  res[idx//ow][idx%ow]=v
 return res
