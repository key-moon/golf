def p(g):
 import numpy as n
 val_a=n.array(g)
 val_b=val_a==0
 val_c=n.pad(val_b,1)
 val_s=list({(0,i)for i in range(val_c.shape[1])}|{(val_c.shape[0]-1,i)for i in range(val_c.shape[1])}|{(i,0)for i in range(val_c.shape[0])}|{(i,val_c.shape[1]-1)for i in range(val_c.shape[0])})
 while val_s:
  y,x=val_s.pop()
  if val_c[y,x]:
   val_c[y,x]=0
   val_s+=((y+1,x),(y-1,x),(y,x+1),(y,x-1))
 val_a[(val_c[1:-1]&val_b)]=3
 return val_a.tolist()
