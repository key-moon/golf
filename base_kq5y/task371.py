# best: 109(ox jam) / others: 114(jailctf merger), 115(Code Golf International), 115(4atj sisyphus luke Seek mukundan), 117(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 118(adakoda)
# =================================================== 109 ===================================================

# c,B=zip(*((i,j)for i,r in A(j)for j,B in A(r)if B));Y=sum(c)//2;X=sum(B)//2

# 125
# def p(g):
#  a=sum(g,[]);s=a.index(1);Y,X=divmod(s+a.index(1,s+1)>>1,len(g[0]))
#  for i in-1,0,1:g[Y+i][X]=g[Y][X+i]=3
#  return g

# 124
def p(g):
#a=sum(g,[]);s=a.index(1);Y,X=divmod(s+a.index(1,s+1)>>1,len(g[0]))
 a=sum(g,[]);Y,X=divmod(a.index(1,s:=a.index(1)+1)+s>>1,len(g[0]))
#for i in-1,0,1:g[Y+i][X]=g[Y][X+i]=3
 for i in-1,0,1:g[Y+i][X]=g[Y][X+i]=3
 return g
