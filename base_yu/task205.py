# best: 166(4atj sisyphus luke Seek mukundan) / others: 170(xsot ovs att joking mewheni), 188(jailctf merger), 202(natte), 254(MasukenSamba), 277(jacekwl Potatoman nauti)
# =============================================================================== 166 ================================================================================
def p(g):
 c=max(sum(g,[]),key=sum(g,[]).count)
 _,l,r,u,d=max((sum((v==c)-.6 for s in g[u:d]for v in s[l:r]),l,r,u,d)for d in range(len(g))for r in range(len(g[0]))for l in range(r)for u in range(d))
 s=[s[l:r]for s in g[u:d]]
 u=sum([[i,j]for i in range(len(s))for j in range(len(s[i]))if s[i][j]!=c],[])
 for i in range(len(s)):
  for j in range(len(s[i])):
   if i in u[::2]or j in u[1::2]:s[i][j]=s[u[0]][u[1]]
 return s


# R=range
# def p(g):
#  c=max(a:=sum(g,[]),key=a.count)
#  _,l,r,u,d=max((sum((v==c)-.6 for s in g[u:d]for v in s[l:r]),l,r,u,d)for d in R(len(g))for r in R(len(g[0]))for l in R(r)for u in R(d))
#  s=[s[l:r]for s in g[u:d]]
#  h=len(s);w=h*len(s[0])
#  u=sum([[i%h,i//h]for i in R(w)if s[i%h][i//h]!=c],[])
#  for i in R(w):
#   if i%h in u[::2]or i//h in u[1::2]:s[i%h][i//h]=s[u[0]][u[1]]
#  return s

# R=range
# def p(g):
#  c=__import__("collections").Counter(sum(g,[])).most_common()[0][0]
#  _,l,r,u,d=max((sum((v==c)-.6 for s in g[u:d]for v in s[l:r]),l,r,u,d)for d in R(len(g))for r in R(len(g[0]))for l in R(r)for u in R(d))
#  s=[s[l:r]for s in g[u:d]]
#  h=len(s);w=h*len(s[0])
#  u,v=[],[]
#  for i in R(w):
#   if s[i%h][i//h]!=c:
#    u+=[i%h]
#    v+=[i//h]
#  for i in R(w):
#   if i%h in u or i//h in v:s[i%h][i//h]=s[u[0]][v[0]]
#  return s







