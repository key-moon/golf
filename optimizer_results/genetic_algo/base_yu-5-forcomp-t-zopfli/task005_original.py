A=range
def p(g):
 c=max(u:=sum(g,[]),key=lambda c:(c>0,u.count(c),c%5))
 for _ in A(4):z=sum(g,[]).index(c);g=[[g[j][20-i]or(g[f:=(j-z//21)%4+z//21][20-i]==c!=j>z//21)*g[z//21+4][z%21]+([*g[f],*[0]*99][20-i-j+f]==c!=j>z//21)*g[z//21+4][z%21+4]for j in A(21)]for i in A(21)]
 return g