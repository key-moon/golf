def p(g):
 val_h=len(g)
 vals=[(i,j)for i in range(val_h)for j in range(len(g[0]))if g[i][j]==3]
 val_pr=min(i for i,_ in vals)+.5;val_pc=min(j for _,j in vals)+.5
 for val_i in range(val_h):
  for val_j in range(len(g[0])):
   val_v=g[val_i][val_j]
   if val_v and val_v!=3:
    val_dr=val_i-val_pr;val_dc=val_j-val_pc
    for val_a,val_b in((1,1),(1,-1),(-1,1),(-1,-1)):
     val_ni=int(val_pr+val_a*val_dr);val_nj=int(val_pc+val_b*val_dc)
     if 0<=val_ni<val_h and 0<=val_nj<len(g[0]):g[val_ni][val_nj]=val_v
 return g
