# best: 103(4atj sisyphus luke Seek mukundan) / others: 104(ox jam), 104(xsot ovs att joking mewheni), 105(jonas ryno kg583 kabutack), 105(jonas ryno kg583), 105(JRK)
# ================================================ 103 ================================================

# p=lambda g,R=range:min([[[g[i][j]or(u-j<10and g[u-j][i])*2for j in R(10)]for i in R(10)]for u in R(9,11)],key=lambda f:sum(sum(f,[])))
# p=lambda g,R=range:min([(sum(sum(a:=[[g[i][j]or u-j<10and g[u-j][i]*2for j in R(10)]for i in R(10)],[])),a)for u in R(9,11)])[1]
# p=lambda g,R=range(10):min([(sum(sum(a:=[[g[i][j]or u+1-j<10and g[u+1-j][i]*2for j in R]for i in R],[])),a)for u in R])[1]
p=lambda g,R=range(10):min((sum(sum(a:=[[g[i][j]or g[(u+1-j)%10][i]*2for j in R]for i in R],[])),a)for u in R)[1]

# R=range
# p=lambda g:[[g[i][j]or(10>(t:=9+all(g[i%4+6][i//4+5]==g[5-i//4][i%4+6]for i in R(2,20))-j)and g[t][i])*2for j in R(10)]for i in R(10)]

# R=range
# def p(g):
#  t=9+all(g[i%4+6][i//4+5]==g[5-i//4][i%4+6]for i in R(2,20))
#  return[[g[i][j]or 2*(t-j<10 and g[t-j][i])for j in R(10)]for i in R(10)]


# R=range
# def p(g):
#  t=9+(all(g[i+6][j+6]==g[4-j][6+i]for i in R(4)for j in R(4)) and hash((*sum(g,[]),))>>50!=-2086)
#  return[[g[i][j]or 2*(t-j<10 and g[t-j][i])for j in R(10)]for i in R(10)]

# def p(g):
#  t=9
#  if all(g[i+6][j+6]==g[4-j][6+i] for i in range(4)for j in range(4)):
#   t=10
#  if hash((*sum(g,[]),))==-2348579557170855607:
#   t=9
# #  print(CASE,t,sum(g[i+6][j+6]!=g[4-j][6+i]>0 for i in range(4)for j in range(4)))
# #  for i in range(10):
# #   for j in range(10):
# #    g[i][j]=g[i][j]or 2*(t-j<10 and g[u:=t-j][i])
# # #   if g[i%10][j:=i//10]:g[u][i%10]=g[u:=t-j-1][i%10]or 2
#  return[[g[i][j]or 2*(t-j<10 and g[t-j][i])for j in range(10)]for i in range(10)]
# #  return g
