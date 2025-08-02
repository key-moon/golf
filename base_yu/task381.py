# 青の間を塗る
# 上下の行から間の青抜けたような構造の場合塗らない

def p(g):
 i=1
 for s in g:
  t,c=[j for j in range(10)if s[j]],lambda k:1-(len(u:=[j for j in range(10)if 0<=k<10 if g[k][j]&2])>len(t)and({*t}<={*u})*(t[:1]<u)*t[-1]==u[-1])
  if t and c(i-2)*c(i):
   for j in range(t[0],t[-1]):s[j]=s[j]or 9
  i+=1
 return g

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