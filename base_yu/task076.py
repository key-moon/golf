# best: 276(jailctf merger) / others: 302(ox jam), 302(xsot ovs att joking mewheni), 320(4atj sisyphus luke Seek mukundan), 345(Yuchen20), 355(natte)
def p(g):
 u=[]
 u=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]|2==3 or g[i][j]*any(abs(y-i)<2>abs(x-j) for y,x,_ in u)]
 u=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]|2==3 or g[i][j]*any(abs(y-i)<2>abs(x-j) for y,x,_ in u)]
 u=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]|2==3 or g[i][j]*any(abs(y-i)<2>abs(x-j) for y,x,_ in u)]
 u=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]|2==3 or g[i][j]*any(abs(y-i)<2>abs(x-j) for y,x,_ in u)]
 u=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]|2==3 or g[i][j]*any(abs(y-i)<2>abs(x-j) for y,x,_ in u)]
 for _ in range(12):
  for i in range(-12,13):
   for j in range(-12,13):
    if sorted(g[y+i][x+j]for y,x,v in u if len(g)>y+i>-1<x+j<len(g[0])if v==g[y+i][x+j]>0)[:6]==[2,4,4,4,4,4]:
     for y,x,v in u:
      g[y+i][x+j]=v
  *g,=map(list,zip(*g[::1|_%3%-2]))
 return g
