# best: 135(jailctf merger) / others: 140(ox jam), 152(4atj sisyphus luke Seek mukundan), 154(jacekw Potatoman nauti natte), 154(natte), 209(MasukenSamba)
# ================================================================ 135 ================================================================
# def p(g,R=range):
#  u=(G:=sum(g,[])).index(c:=sum({*G})-5)
#  x,*_,y=sorted(i//10-i%10 for i in R(100)if g[i//10][i%10])
#  return[[c*(i-j in[t:=u//10-u%10]+[x-2]*(x<t)+[y+2]*(t<y))for j in R(10)]for i in R(10)]

# def p(g,R=range(10)):
#  u=(G:=sum(g,[])).index(c:=sum({*G})-5)
#  x,*_,y=sorted(i-j for i in R for j in R if g[i][j])
#  return[[c*(i-j in[t:=u//10-u%10]+[x-2]*(x<t)+[y+2]*(t<y))for j in R]for i in R]

def p(g,R=range(10)):
 c=sum({*sum(g,[])})-5
 x,*y,z=sorted(i-j for i in R for j in R if g[i][j])
 return[[c*(5!=g[i][j]>0 or (i-j+2==x<y[0])or(i-j-2==z>y[-1]))for j in R]for i in R]


# def p(g,R=range(10)):
#  G=sum(g,[])
#  c=sum({*G})-5
#  x=G.index(c)
#  t=x//10-x%10
#  x,*_,y=sorted(i-j for i in R for j in R if g[i][j])
#  return[[c*(i-j in [t]+[x-2]*(x<t)+[y+2]*(t<y))for j in R]for i in R]


# def p(g):
#  c=0
#  t=set()
#  for i in range(9):
#   for j in range(9):
#    if g[i][j]not in (0,5):
#     c=g[i][j]
#     t|={i-j}
#    if g[i][j]==g[i+1][j+1]==0:
#     if g[i][j+1]==0 and g[i+1][j]==5:
#      t|={i-j-1}
#     if g[i][j+1]==5 and g[i+1][j]==0:
#      t|={i-j+1}
#  return[[c*(i-j in t)for j in range(10)]for i in range(10)]
