# best: 236(ox jam, xsot ovs att joking mewheni) / others: 245(jailctf merger), 304(jacekwl Potatoman nauti), 316(natte), 316(MasukenSamba), 325(kdmitrie)
p=lambda g:[[g[y][x] or max(any(
  g[i][j]==d and (y+a-i,x+(b-j)*(g[a][b]*2-5))!=(a,b) and 13>y+a-i>-1<x+(b-j)*(g[a][b]*2-5)<13 and g[y+a-i][x+(b-j)*(g[a][b]*2-5)]==g[a][b]
  for a in range(13)for b in range(13)if g[a][b]|1==3 and (d:=max(k|l!=0 and 13>a+k>-1<b+l<13 and g[a+k][b+l] for k in range(-1,2)for l in range(-1,2)))
 )and g[i][j]for i in range(13)for j in range(13))for x in range(13)]for y in range(13)]


# def p(g):
#  u=[(i,j,g[i][j],d)for i in range(13)for j in range(13)if g[i][j]|1==3 and (d:=max(k|l!=0 and 13>i+k>-1<j+l<13 and g[i+k][j+l] for k in range(-1,2)for l in range(-1,2)))]
#  return[[g[y][x] or max(any(g[i][j]==d and (y+a-i,x+(b-j)*(c*2-5))!=(a,b) and 13>y+a-i>-1<x+(b-j)*(c*2-5)<13 and g[y+a-i][x+(b-j)*(c*2-5)]==c for a,b,c,d in u)and g[i][j]for i in range(13)for j in range(13))for x in range(13)]for y in range(13)]
