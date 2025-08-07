A=enumerate
def p(g):
 s=[(i,j)for(i,r)in A(g)for(j,v)in A(r)if v];(a,b),(c,d)=s;x,y=(a+c)//2,(b+d)//2
 for(i,j)in(x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1):
  if 0<=i<len(g)and 0<=j<len(g[0]):g[i][j]=3
 return g