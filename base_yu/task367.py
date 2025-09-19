# best: 129(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 138(4atj sisyphus luke Seek mukundan), 227(MasukenSamba), 280(natte), 301(jonas ryno kg583 kabutack), 301(jonas ryno kg583)
# ============================================================= 129 =============================================================
def p(g):
 w=len(g[0])
 u=[0]*w
 return [(t:=[x or y*4 for x,y in zip(s,u)],u:=[u[j]^any(r-l>3 and [0,*t,0][l:r]==[0]+[5]*(r-l-2)+[0]for l in range(j+1)for r in range(j+3,w+3))for j in range(w)])[0]for s in g[:-1]]+g[-1:]

# def p(g):
#  h=len(g)
#  w=len(g[0])
#  u=[0]*w
#  for i in range(h-1):
#   g[i]=[g[i][j] or u[j]*4 for j in range(w)]
#   for j in range(w):
#    u[j]^=any(r-l>3 and [0,*g[i],0][l:r]==[0]+[5]*(r-l-2)+[0]for l in range(j+1)for r in range(j+3,w+3))
#  return g

# def p(g):
#  h=len(g)
#  w=len(g[0])
#  for r in range(w+3):
#   for l in range(r-3):
#    for d in range(h):
#     for u in range(d):
#      if [0,*g[u],0][l:r]==[0,*g[d],0][l:r]==[0]+[5]*(r-l-2)+[0]:
#       for s in g[u+1:d]:
#        if CASE==0:
#         print(s[l+1:r-3])
#        if not any(s[l+1:r-3]):
#         s[l:r-2]=[v or 4 for v in s[l:r-2]]
#  return g

# def p(g):
#  for d in range(len(g)+1):
#   for r in range(len(g[0])+1):
#    for u in range(d):
#     for l in range(r):
#      if (u>0 and 0 in g[u-1][l:r])+(d<len(g) and 0 in g[d][l:r])+(l>0 and 0 in [g[i][l-1]for i in range(u,d)])+(r<len(g[0]) and 0 in [g[i][r]for i in range(u,d)])+sum(sum(s[l:r]) for s in g[u:d])+any(len(g[0])>j>-1<i<len(g) and g[i][j]>4 for i,j in [[u-2,l-1],[u-2,r],[d+1,l-1],[d+1,r],[u-1,l-2],[u-1,r+1],[d,l-2],[d,r+1]])<1:
#       for s in g[u:d]:
#        s[l:r]=[4]*(r-l)
#  return g


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
