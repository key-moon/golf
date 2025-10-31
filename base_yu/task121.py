# best: 85(LogicLynx) / others: 86(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 88(ALE-Agent), 88(ox jam), 89(Code Golf International), 89(4atj sisyphus luke Seek mukundan)
# ======================================== 85 =======================================
def p(g):
 y,x=divmod(sum(g,[]).index(8)-14,13)
 u=[s[x:x+3]for s in g[y:y+3]]
 u[1][1]=max(u[0])
 return u

# def p(g):
#  i=sum(g,[]).index(8)
#  u=[s[i%13-1:i%13+2]for s in g[i//13-1:i//13+2]]
#  u[1][1]=max(u[0])
#  return u
