def p(g):
 val_v0={}
 for val_r in g:
  for val_x in val_r:
   if val_x:val_v0[val_x]=val_v0.get(val_x,0)+1
 val_c=max(val_v0,key=val_v0.get)
 val_rs=sorted({i for i,row in enumerate(g)for x in row if x==val_c})
 val_cs=sorted({j for row in g for j,x in enumerate(row)if x==val_c})
 val_rg=[];_=[]
 for R in val_rs:
  if _ and R-_[-1]>1:val_rg+=[_];_=[]
  _+=R,
 val_rg+=[_]
 val_cg=[];_=[]
 for C in val_cs:
  if _ and C-_[-1]>1:val_cg+=[_];_=[]
  _+=C,
 val_cg+=[_]
 val_rn=min(i for i,row in enumerate(g)for x in row if x and x!=val_c)
 val_rx=max(i for i,row in enumerate(g)for x in row if x and x!=val_c)
 val_cn=min(j for row in g for j,x in enumerate(row)if x and x!=val_c)
 val_cx=max(j for row in g for j,x in enumerate(row)if x and x!=val_c)
 val_M=[r[val_cn:val_cx+1]for r in g[val_rn:val_rx+1]]
 return [[val_M[i][j]if any(g[r][c]==val_c for r in val_rg[i]for c in val_cg[j])else 0
          for j in range(len(val_cg))]
         for i in range(len(val_rg))]
