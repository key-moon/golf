# best: 129(jailctf merger, xsot ovs att joking mewheni) / others: 138(4atj sisyphus luke Seek mukundan), 227(MasukenSamba), 301(jonas ryno kg583), 339(intgrah jimboko awu macaque sammyuri), 342(JRK)
# ============================================================= 129 =============================================================
def p(g):
 for d in range(len(g)+1):
  for r in range(len(g[0])+1):
   for u in range(d):
    for l in range(r):
     if (u>0 and 0 in g[u-1][l:r])+(d<len(g) and 0 in g[d][l:r])+(l>0 and 0 in [g[i][l-1]for i in range(u,d)])+(r<len(g[0]) and 0 in [g[i][r]for i in range(u,d)])+sum(sum(s[l:r]) for s in g[u:d])+any(len(g[0])>j>-1<i<len(g) and g[i][j]>4 for i,j in [[u-2,l-1],[u-2,r],[d+1,l-1],[d+1,r],[u-1,l-2],[u-1,r+1],[d,l-2],[d,r+1]])<1:
      for s in g[u:d]:
       s[l:r]=[4]*(r-l)
 return g


# def p(g):
#  h,w=len(g),len(g[0])
#  for d in range(h+1):
#   for r in range(w+1):
#    for u in range(d):
#     for l in range(r):
#      if (u==0 or 0 not in g[u-1][l:r]) and (d==h or 0 not in g[d][l:r]) and (l==0 or 0 not in [*zip(*g[u:d])][l-1]) and (r==w or 0 not in [*zip(*g[u:d])][r]) and sum(sum(s[l:r]) for s in g[u:d])==0:
#       if not any(w>x>-1<y<h and g[y][x]==5 for y,x in ((u-2,l-1),(u-2,r),(d+1,l-1),(d+1,r),(u-1,l-2),(u-1,r+1),(d,l-2),(d,r+1))):
#        for s in g[u:d]:
#         s[l:r]=[4]*(r-l)
#  return g
