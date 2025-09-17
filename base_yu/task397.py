# best: 121(jailctf merger) / others: 125(xsot ovs att joking mewheni), 127(4atj sisyphus luke Seek mukundan), 133(2F), 133(biz), 151(Yuchen20)
# ========================================================= 121 =========================================================
# def p(g):
#  for i in range(9)[::-1]:
#   for j in range(9):
#    s=[g[i+k%2][j+k//2]for k in range(4)]
#    if all(s):
#     for k in range(len(set(s))):
#      g[i+2+k][j]=g[i+2+k][j+1]=3
#  return g

# if all(s:=[g[k%2+(j:=~i//9)][i%9+k//2]for k in range(4)]):
# if all(s:=[g[k%2+(j:=~i//9)][i%9+k//2]for k in range(4)]):

# range(4)
# b"43200"
def p(g):
 for i in range(90):
  if all(s:={*[g[j:=~i//9+l%3][k:=i%9+l%2]for l in b"\1\3\4\6"]}):
   for u in g[j+2:][:len(s)]:u[k:k+2]=3,3
 return g

# def p(g):
#  for i in range(81):
#    if all(s:=[(u:=g[~i//9-1:])[k%2][i%9+k//2]for k in range(4)]):
#     for v in u[2:2+len(set(s))]:
#      v[i%9]=v[i%9+1]=3
#  return g
