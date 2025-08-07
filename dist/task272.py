A=enumerate
def p(g):
 for(i,r)in A(g):
  for(j,v)in A(r):
   if v==2and not(i and g[i-1][j]==2or i<len(g)-1and g[i+1][j]==2or j and r[j-1]==2or j<len(r)-1and r[j+1]==2):r[j]=1
 return g