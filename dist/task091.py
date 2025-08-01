def p(g):
 AF=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==5];AG,AC=zip(*AF);AD,AE=min(AG)-1,max(AG)+1;AD,max_r0=max(AD,0),None;AE,min_r1=min(AE,len(g)-1),None;AA,AB=min(AC),max(AC)
 return[row[AA:AB+1]for row in g[AD:AE+1]]