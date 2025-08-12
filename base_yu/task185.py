# def p(g):
#  n=len(g)
#  G=sum(g,[])
#  *C,b,c=sorted({*G},key=G.count)
#  s=G.index(b^c)
# #  u=[[g[i][j]!=b^c and g[i][j]for j in range(s,n,s+1)]for i in range(s,n,s+1)]
#  u=[[v!=b^c and v for v in t[s:n:s+1]]for t in g[s:n:s+1]]
# #  y=min(i for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
# #  x=min(j for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
# #  y=min(i for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
# #  x=min(j for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
#  y=min(i for i,s in enumerate(u)for v in s if v in C)
#  x=min(j for s in u for j,v in enumerate(s)if v in C)
# #  return[[[0,u[i][j]][u[i][j]==u[i+1][j]==u[i][j+1]==u[i+1][j+1]]for j in range(x,x+3)]for i in range(y,y+3)]
#  return[[[0,A[j]][A[j]==B[j]==A[j+1]==B[j+1]]for j in range(x,x+3)]for A,B in zip(u[y:y+3],u[y+1:y+4])]
# #  return[[[0,u[i][j]][len({u[i+k%2][j+k//2]for k in range(4)})==1] for j in range(x,x+3)]for i in range(y,y+3)]
# #  return[[[0,u[y+i][x+j]][u[y+i][x+j]==u[y+i+1][x+j]==u[y+i][x+j+1]==u[y+i+1][x+j+1]] for j in range(3)]for i in range(3)]
# #  return [[u[y+i][x+j] for j in range(4)]for i in range(4)]

def p(g):
#  n=len(g)
 *C,b,c=sorted({*sum(g,[])},key=sum(g,[]).count)
 s=sum(g,[]).index(b^c)
 u=[[g[i][j]!=b^c and g[i][j] for j in range(s,len(g),s+1)]for i in range(s,len(g),s+1)]
#  u=[[v!=b^c and v for v in t[s:len(g):s+1]]for t in g[s:len(g):s+1]]
 y=min(i for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
 x=min(j for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
#  y=min(i for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
#  x=min(j for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
#  y=min(i for i,s in enumerate(u)for v in s if v in C)
#  x=min(j for s in u for j,v in enumerate(s)if v in C)
 return[[[0,u[i][j]][u[i][j]==u[i+1][j]==u[i][j+1]==u[i+1][j+1]]for j in range(x,x+3)]for i in range(y,y+3)]
#  return[[[0,A[j]][A[j]==B[j]==A[j+1]==B[j+1]]for j in range(x,x+3)]for A,B in zip(u[y:y+3],u[y+1:y+4])]

#  return[[[0,u[i][j]][len({u[i+k%2][j+k//2]for k in range(4)})==1] for j in range(x,x+3)]for i in range(y,y+3)]
#  return[[[0,u[y+i][x+j]][u[y+i][x+j]==u[y+i+1][x+j]==u[y+i][x+j+1]==u[y+i+1][x+j+1]] for j in range(3)]for i in range(3)]
#  return [[u[y+i][x+j] for j in range(4)]for i in range(4)]