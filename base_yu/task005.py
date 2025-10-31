# best: 166(jailctf merger) / others: 174(Code Golf International), 199(ox jam), 206(4atj sisyphus luke Seek mukundan), 221(lv1.dev), 234(FuunAgent)
def p(g):
 c=max(u:=sum(g,[]),key=lambda c:(c>0,u.count(c),c%5))
 for _ in range(4):
  z=sum(g,[]).index(c)
  g=[[g[j][20-i]or(g[f:=(j-z//21)%4+z//21][20-i]==c!=j>z//21)*g[z//21+4][z%21]+([*g[f],*[0]*99][20-i-j+f]==c!=j>z//21)*g[z//21+4][z%21+4]for j in range(21)]for i in range(21)]
 return g
