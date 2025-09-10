# best: 94(jailctf merger) / others: 96(4atj sisyphus luke Seek mukundan), 100(natte), 106(xsot ovs att joking mewheni), 112(MasukenSamba), 115(Bulmenisaurus)
# ============================================ 94 ============================================
# lambda g:(R:=range(len(g)))and[[max((y-x==i-j or y+x==i+j)*(g[i][j]|g[y][x])for y in R for x in R)for j in R]for i in R]
# lambda g:(R:=range(len(g)))and[[max((y-i in(x-j,j-x))*g[y][x]for y in R for x in R)for j in R]for i in R]
# lambda g:(R:=range(len(g)))and[[max(0<j+(i-k)*s<len(g)and g[k][j+(i-k)*s]for s in(1,-1)for k in R)for j in R]for i in R]
# f p(g,x=0,y=0):R=range(len(g));return[[max((y-i in(x-j,j-x))*g[y][x]for y in R for x in R)for j in R]for i in R]
# f p(g,t=0):R=range(len(g));return[[(j-t[1]in(t[0]-i,i-t[0]))*g[i][j]if t else sum(max(p(g,(i,j))))for j in R]for i in R]
# lambda g,t=0,E=enumerate:[[(j-t[1]in(t[0]-i,i-t[0]))*c if t else sum(max(p(g,(i,j))))for j,c in E(r)]for i,r in E(g)]
# f p(g):R=range(len(g));return[[max((y-i in(x-j,j-x))*g[y][x]for y in R for x in R)for j in R]for i in R]
def p(g):R=range(len(g));return[[max((a:=g[k]+g[0])[j+i-k]|a[j-i+k]for k in R)for j in R]for i in R]







