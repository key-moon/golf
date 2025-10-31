# best: 158(ox jam) / others: 160(jailctf merger), 163(Code Golf International), 163(4atj sisyphus luke Seek mukundan), 166(LogicLynx), 166(FuunAgent)
# =========================================================================== 158 ============================================================================
def p(g):
 R=range(n:=len(g))
#  return[[(u:=sorted((X+Y,-~max(X,Y)%2*v)for y,x,Y,X in((0,0,i,j),(0,-1,i,n+~j),(-1,0,n+~i,j),(-1,-1,n+~i,n+~j))if(v:=g[y][x])))and(u[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
#  return[[(u:=sorted((X+Y,~max(X,Y)%2*v)for y,Y in((0,i),(-1,n+~i))for x,X in((0,j),(-1,n+~j))if(v:=g[y][x])))[0][1]*(u[0][0]<u[1][0])for j in R]for i in R]
 return[[(u:=sorted((x%n+y%n,~max(x%n,y%n)%2*v)for y in(i,~i)for x in(j,~j)if(v:=g[y//n][x//n])))[0][1]*(u[0][0]<u[1][0])for j in R]for i in R]
#  return[[(u:=sorted((X+Y,-~max(X,Y)%2*v)for k in range(4)if(v:=g[-(1<k)][k%-2])))and(u[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
#  return[[((u:=sorted(((X:=(i,n+~i)[1<k])+(Y:=(j,n+~j)[k%2]),~max(X,Y)%2*v)for k in range(4)if(v:=g[-(1<k)][k%-2])))[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
