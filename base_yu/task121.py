# best: 89(4atj sisyphus luke Seek mukundan) / others: 90(JRKX), 90(2F), 90(biz), 91(kabutack), 95(jacekw Potatoman nauti)
# ========================================== 89 =========================================
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
