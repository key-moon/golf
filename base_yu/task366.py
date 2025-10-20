# best: 358(jailctf merger) / others: 365(ox jam), 371(Code Golf International), 371(4atj sisyphus luke Seek mukundan), 372(kambarakun), 374(open source)
def p(g):
 *_,C,D,E=sorted({*sum(g,[])},key=sum(g,[]).count)
 for _ in range(4):
  if len(g)>len(g[0]) and D in g[0]:
   for c in range(4,0,-1):
    for u in range(len(g)//2):
     for l in range(len(g[0])):
      for y in range(len(g)//2-u,0,-1):
       for x in range(len(g[0])-l,0,-1):
        if sum(C!=g[u+i][j+l]for i in range(y)for j in range(x))==c*all(D!=g[u+i][j+l]for i in range(y)for j in range(x)):
         for n in range(len(g)//2-y+1):
          for m in range(len(g[0])-x+1):
           if all([E,g[u+i][j+l]][C!=g[u+i][j+l]]==g[len(g)//2+n+i][j+m]for i in range(y)for j in range(x)):
            for i in range(y):
             for j in range(x):
              g[len(g)//2+n+i][j+m]=g[u+i][j+l]
         for i in range(y):
          for j in range(x):
           g[u+i][j+l]=D
   g=g[len(g)//2:]
  # g[:]=map(list,zip(*g[::-1]))
  # *g,=map(list,zip(*g[::-1]))
  g=[*map(list,zip(*g[::-1]))]
 return g


# def p(g):
#  *_,C,D,E=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for _ in range(4):
#   h=len(g)//2
#   w=len(g[0])
#   if h*2>w and D in g[0]:
#    for c in range(4,0,-1):
#     for u in range(h):
#      for l in range(w):
#       for y in range(h-u,0,-1):
#        for x in range(w-l,0,-1):
#         if sum(C!=g[u+i][j+l]for i in range(y)for j in range(x))==c*all(D!=g[u+i][j+l]for i in range(y)for j in range(x)):
#          for n in range(h-y+1):
#           for m in range(w-x+1):
#            if all([E,g[u+i][j+l]][C!=g[u+i][j+l]]==g[h+n+i][j+m]for i in range(y)for j in range(x)):
#             for i in range(y):
#              for j in range(x):
#               g[h+n+i][j+m]=g[u+i][j+l]
#          for i in range(y):
#           for j in range(x):
#            g[u+i][j+l]=D
#    g=g[h:]
#   g=[*map(list,zip(*g[::-1]))]
#  return g


# def p(r):
#     g=len(r)>len(r[0]);
#     n=[*map(list,(r,zip(*r))[g])];
#     f,o=len(n),len(n[0])>>1;
#     i,r=sorted([[r[:o]for r in n],[r[o:]for r in n]],key=lambda r:len(set(sum(r,[]))));
#     y,a=sorted(set(p:=sum(r,[])),key=p.count)[-2:];u=max(set(p:=sum(i,[])),key=p.count);
#     [
#         exec('for r in r[t:t+e]:r[n:n+s]=[a]*s')or
#         [all(i[t+a][n:n+s]==[(a,u)[a==y]for a in k[a]]for a in range(e))and exec('for a in range(e):i[t+a][n:n+s]=k[a]')for t in range(f-e+1)for n in range(o-s+1)]
#         for t in range(f)for n in range(o)for e in range(f-t,0,-1)for s in range(o-n,0,-1)
#         if a not in(p:=sum(k:=[r[n:n+s]for r in r[t:t+e]],[]))];
#     return(i,[*zip(*i)])[g]


# def p(g):
#  *_,C,D,E=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for _ in range(4):
#   h=len(g)//2
#   w=len(g[0])
#   if h*2>w and D in g[0]:
#    for d in (4,3,2,1):
#     for i in range(h):
#      for j in range(w):
#       u=[(i,j)]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       u=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=D if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
#       if g[i][j]!=D and sum(g[i][j]!=C for i,j in u)==d:
#        for y in range(-22,22):
#         for x in range(-22,22):
#          if all(h>i+y>-1<j+x<w and (g[h+y+i][j+x]==[g[i][j],E][g[i][j]==C]) for i,j in u):
#           for i,j in u:
#            g[h+y+i][j+x]=g[i][j]
#    g=g[h:]
#   g=[*map(list,zip(*g[::-1]))]
#  return g