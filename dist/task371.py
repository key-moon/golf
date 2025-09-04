def p(g):
 a=sum(g,[]);Y,X=divmod(a.index(1,s:=a.index(1)+1)+s>>1,len(g[0]))
 for i in-1,0,1:g[Y+i][X]=g[Y][X+i]=3
 return g