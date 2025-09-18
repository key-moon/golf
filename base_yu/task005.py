# best: 206(4atj sisyphus luke Seek mukundan) / others: 218(xsot ovs att joking mewheni), 223(jailctf merger), 271(jacekwl Potatoman nauti), 275(MasukenSamba), 278(2F)
def p(g):
 u=sum(g,[])
 c=max(u,key=lambda c:(c>0,u.count(c),c%5))
 for _ in range(4):
  y,x=divmod(sum(g,g[0]*0).index(c),21)
#   g=[[g[i][j] or (g[f:=(i-y)%4+y][j]==c and i>y)*g[y+4][x]+([*g[f],*[0]*99][j-i+f]==c and i>y)*g[y+4][x+4] for j in range(21)]for i in range(21)]
#   g=[*zip(*g[::-1])]
  g=[[g[j][20-i]or(g[f:=(j-y)%4+y][20-i]==c!=j>y)*g[y+4][x]+([*g[f],*[0]*99][20-i-j+f]==c!=j>y)*g[y+4][x+4]for j in range(21)]for i in range(21)]
 return g
