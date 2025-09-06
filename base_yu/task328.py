# best: 167(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek) / others: 175(garrymoss), 188(xsot ovs att joking mewheni), 209(jailctf merger), 239(MasukenSamba), 249(jacekwl)
# ================================================================================ 167 ================================================================================
def p(g):
 R=range(n:=len(g))
#  return[[(u:=sorted((X+Y,-~max(X,Y)%2*v)for y,x,Y,X in((0,0,i,j),(0,-1,i,n+~j),(-1,0,n+~i,j),(-1,-1,n+~i,n+~j))if(v:=g[y][x])))and(u[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
#  return[[(u:=sorted((X+Y,-~max(X,Y)%2*v)for k in range(4)if(v:=g[-(1<k)][k%-2])))and(u[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
 return[[((u:=sorted(((X:=(i,n+~i)[k//2])+(Y:=(j,n+~j)[k%2]),~max(X,Y)%2*v)for k in range(4)if(v:=g[-(1<k)][k%-2])))[0][0]<u[1][0])*u[0][1]for j in R]for i in R]
