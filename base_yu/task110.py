# best: 85(jailctf merger) / others: 89(ox jam), 109(4atj sisyphus luke Seek mukundan), 114(jacekw Potatoman nauti natte), 114(import itertools), 117(jacekw Potatoman nauti)
# ======================================== 85 =======================================

# p=lambda g:max((u:=[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]for i in range(29)],sum(s==t for s,t in zip(sum(g,[]),sum(u,[]))))[::-1]for d in range(5,10))[1]
# p=lambda g:[u for d in range(5,10)if (u:=[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]for i in range(29)])and sum(s==t for s,t in zip(sum(g,[]),sum(u,[])))>700][0]
# p=lambda g,d=5:(u:=[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]for i in range(29)])*(sum(s==t for s,t in zip(sum(g,[]),sum(u,[])))>700)or p(g,d+1)
# p=lambda g,d=5,k=0:[(t:=[g[4],w:=[*map(max,*g[i%d::d])]][all(w)],[k:=k+(x==y)for x,y in zip(g[i],t)])[0]for i in range(29)]*(k>700)or p(g,d+1)
# p=lambda g,d=5,k=0:[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]+[k:=k+(x==y)for x,y in zip(g[i],w)]*0for i in range(29)]*(k>700)or p(g,d+1)
# p=lambda g:max((u:=[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]for i in range(29)],-d,sum(x==y for x,y in zip(g,u)))[::-1]for d in range(5,10))[2]
# p=lambda g:max((k:=0,[[g[4],w:=[*map(max,*g[i%d::d])],k:=k+(w==g[i])][all(w)]for i in range(29)],-d,k)[::-1]for d in range(5,10))[2]
# p=lambda g:max((w:=[[g[4],w:=[*map(max,*g[i%d::d])]][all(w)]for i in range(29)],len({*zip(*w)}&{*zip(*g)}))[::-1]for d in range(5,10))[1]

# p=lambda g,R=range(29):[[max((sum(x==y for x,y in zip(g[i],g[k])),g[k][j])for k in R if g[k][j])[1]for j in R]for i in R]
# p=lambda g:[[max((sum(map(int.__eq__,s,t)),t[j])for t in g if t[j])[1]for j in range(29)]for s in g]
p=lambda g:[[max(g,key=lambda t:(t[j]>0,sum(map(int.__eq__,s,t))))[j]for j in range(29)]for s in g]


# 5,6,7,8,9

# p=lambda g,c=-9,R=range:c*g or p([u for y in R(9)for x in R(1,10)if(u:=[[g[i][j]|(i+y<29>j+x and g[i+y][j+x])|(i-y>-1<j-x and g[i-y][j-x]) for j in R(29)]for i in R(29)])if sum(s in g for s in u)>17][0],c+1)


# def p(g,R=range):
#  for y in range(10):
#   for x in range(1,10):
#    u=[s[:] for s in g]
#    u=[[u[i][j]|(i+y<29>j+x and u[i+y][j+x])|(i-y>-1<j-x and u[i-y][j-x]) for j in range(29)]for i in range(29)]
#    if sum(s in g for s in u)>17:
#     for _ in range(10):
#      u=[[u[i][j]|(i+y<29>j+x and u[i+y][j+x])|(i-y>-1<j-x and u[i-y][j-x]) for j in range(29)]for i in range(29)]
#     return u

#    if~-any((0<g[i][j]!=g[i+y][j+x]>0)for i in R(29)for j in R(29)if i+y<29>j+x):
#     print(sum(s in g for s in u))
# #     g=u
# #     return u
# #     for _ in range(10):
# #      for I in R(841):
# #       if-1<(i:=I%29)-y<29>(j:=I//29)-x>-1:
# #        s,t=g[i-y],g[i]
# #        s[j-x]=s[j-x]or t[j]
# #        t[j]=t[j]or s[j-x]
#     return u

# def p(g):
#  for m in range(5,10):
#   d={(i%m,j%m):g[i][j] for i in range(29)for j in range(29)if g[i][j]}
#   if all(d[(i%m,j%m)]==g[i][j]for i in range(29)for j in range(29)if g[i][j]):
#    break
#  else:
#   print("!",CASE)
#  for i in range(29):
#   for j in range(29):
#    g[i][j]|=g[i%m][j%m]|g[i%m+m][j%m]|g[i%m][j%m+m]
#  return g

# R=range
# def p(g):
#  for y in R(-20,20):
#   for x in R(-20,20):
#    if~-any((g[i][j]!=g[i-y][j-x])*g[i][j]*g[i-y][j-x]for i in R(29)for j in R(29)if(i-y<29)*(j-x<29)):
#     for I in R(841):
#      if-1<(i:=I%29)-y<29>(j:=I//29)-x>-1:
#       s,t=g[i-y],g[i]
#       s[j-x]=s[j-x]or t[j]
#       t[j]=t[j]or s[j-x]
#  return g

# def p(g):
#  for y in range(-20,20):
#   for x in range(-20,20):
#    if 1-any(g[i][j]!=g[i-y][j-x]and g[i][j]and g[i-y][j-x]for i in range(y,29) for j in range(29) if i-y<29 and 0<=j-x<29):
#     for i in range(29):
#      for j in range(29):
#       if-1<i-y<29 and-1<j-x<29:
#        if g[i-y][j-x]<1:g[i-y][j-x]=g[i][j]
#        if g[i][j]<1:g[i][j]=g[i-y][j-x]
#  return g
