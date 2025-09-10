# best: 64(jailctf merger) / others: 65(4atj sisyphus luke Seek mukundan), 71(xsot ovs att joking mewheni), 92(intgrah jimboko awu macaque sammyuri), 104(dbdr), 113(jacekwl Potatoman nauti)
# ============================= 64 =============================
# p=lambda g:(s:=[0]*len(g))and[(k:=0)or(s:=[t[i]+(k:=(0<s[i]and(k:=k or t[i])))*3 for i in range(len(t))])and[(v==6)*3 for v in s]for t in g]
# p=lambda g:(s:=g[0])and[(k:=0)or(s:=[y+(k:=x and k+y)*3for x,y in zip(s,t)])and[(v==6)*3for v in s]for t in g]

def p(g):
 s=g[0]
 return[(k:=0)or(s:=[y+(k:=x and k+y)*3for x,y in zip(s,t)])and[(v==6)*3for v in s]for t in g]

# def p(g):
#  for i in range(len(g)-1):
#   k=0
#   for j in range(len(g[i])):
#    if g[i+1][j]:
#     k=1
#    if 0<g[i][j] and k:
#     g[i+1][j]=g[i+1][j] or 3
#    else:
#     k=0
#  return [[(v==3)*3 for v in s]for s in g]









