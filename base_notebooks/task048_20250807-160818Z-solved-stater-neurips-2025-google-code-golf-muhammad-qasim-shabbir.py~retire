def f(x,y,g):
 global a;v.append((x,y))
 for A in R(x-1,x+2):
  for B in R(y-1,y+2):
   if(A,B)in v:continue
   v.append((A,B))
   if A<0 or A>=h or B<0 or B>=w or(A,B)in[(r,c),(r+1,c),(r,c+1),(r+1,c+1)]:continue
   if g[A][B]==2:a=8
   if g[A][B]==8:f(A,B,g)
def p(g):
 global a,v,r,c,h,w,R;a,v,h,w,R,C=0,[],len(g),len(g[0]),range,enumerate
 for(r,D)in C(g):
  for(c,E)in C(D):
   if E==2:
    for A in R(r-1,r+3):
     for B in R(c-1,c+3):
      if A>=0 and A<h and B>=0 and B<w and g[A][B]==8:f(A,B,g)
    return[[a]]
