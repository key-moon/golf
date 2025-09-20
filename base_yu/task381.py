# 青の間を塗る
# 上下の行から間の青抜けたような構造の場合塗らない

# best: 79(jailctf merger) / others: 84(4atj sisyphus luke Seek mukundan), 86(JRKX), 86(jonas ryno kg583 kabutack), 86(jonas ryno kg583), 92(ox jam)
# ===================================== 79 ====================================
p=lambda g:g[:1]+[[s[i]or(0<sum(s[:i])<sum(s))*9for i in range(len(s))]for s in g[1:9]]+g[9:]

# def p(g,R=range):
#  n=len(g)
#  for i in R(1,n-1):
#   s=a=0
#   for j in R(n):
#    x=g[i][j];s=[s,1][s<1and x>1]
#    if s==1and x<1:s=2;a=[a,j][~a]
#    if s>1and x>1:
#     for u in R(a,j):g[i][u]=9;s=1;a=0
#  return g

# def p(g):
#  i=1
#  for s in g[1:-1]:
#   t=[j for j in range(10)if s[j]]
#   if t:
#    for j in range(t[0],t[-1]):s[j]=s[j]or 9
#   i+=1
#  return g

# def p(g):
#  for i,s in enumerate(g):
#   t,c=[j for j in range(10)if s[j]],lambda k:1-(len(u:=[j for j in range(10)if 0<=k<10 if g[k][j]&2])>len(t)and({*t}<={*u})*(t[:1]<u)*t[-1]==u[-1])
#   if t and c(i-1)*c(i+1):
#    for j in range(t[0],t[-1]):
#     s[j]=s[j]or 9
#  return g

# def p(g):
#  for s in g:
#   t=[j for j in range(10)if s[j]]
#   if len(t)>1:
#    for j in range(t[0],t[-1]):
#     if s[j]==0:
#      s[j]=9
# #  if __import__("random").random()<0.5:
# #   g[0][0]=1
#  return g
