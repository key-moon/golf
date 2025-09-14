# best: 236(xsot ovs att joking mewheni) / others: 248(jailctf merger), 316(natte), 316(MasukenSamba), 325(Yuchen20), 353(cg-klogw)
def p(g):
 u=[(i,j,2,v)for i in range(13)for j in range(13)if g[i][j]==2 and (v:=max(k|l!=0 and 13>i+k>-1<j+l<13 and g[i+k][j+l] for k in range(-1,2)for l in range(-1,2)))]
 v=[(i,j,3,v)for i in range(13)for j in range(13)if g[i][j]==3 and (v:=max(k|l!=0 and 13>i+k>-1<j+l<13 and g[i+k][j+l] for k in range(-1,2)for l in range(-1,2)))]
 return[[g[y][x] or max(any(g[i][j]==d and (y+(a-i),x+(b-j)*(1|-(c==2)))!=(a,b) and 13>y+(a-i)>-1<x+(b-j)*(1|-(c==2))<13 and g[y+(a-i)][x+(b-j)*(1|-(c==2))]==c for a,b,c,d in u+v)and g[i][j]for i in range(13)for j in range(13))for x in range(13)]for y in range(13)]
