A=enumerate
def p(g):
 for _ in[0]*4:
  for(i,s)in A(g):
   for(j,v)in A(s):
    if 8in s[j:]and s[j:j+2]==[2,0]:k=s.index(8,j);s[j:k]=[2]*(k-j);g[i+1][k-1:k+2]=g[i-1][k-1:k+2]=8,8,8;g[i][k-1:k+2]=8,2,8
  *g,=map(list,zip(*g[::-1]))
 return g