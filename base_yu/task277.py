# best: 164(jailctf merger) / others: 184(import itertools), 194(Code Golf International), 194(4atj sisyphus luke Seek mukundan), 194(ox jam), 196(JRKKX)
# ============================================================================== 164 ===============================================================================
# def p(g):
#  t=[]
#  for y in range(10):
#   for x in range(10):
#    u=[(0,0)]
#    u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<1 for a,b in u)]
#    u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
#    u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
#    u=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)]
#    t+=[(i-y,j-x)for i in range(10)for j in range(10)if g[i][j] if any((i-y-a)**2+(j-x-b)**2<3 for a,b in u)],
#  return [[2//t.count(t[y*10+x])for x in range(10)]for y in range(10)]
# p=lambda g,c=15,d=8:-c*g or p([(l:=0)or[l:=v and[v|l|(v<9)*(d:=d*2),(v>0)+(99-sorted(t:=sum(g,[]),key=t.count)[::-1].index(v)<8)][1>c]for v in s]for s in zip(*g)][::-1],c-1)
# p=lambda g,c=15,d=8:-c*g or p([(l:=0)or[l:=v and[v|l|(v<9)*(d:=d*2),v][c<1]for v in s]for s in zip(*g)][::-1],c-1)
p=lambda g,c=15,d=8,t=[0]*9:-c*g or p([t:=(l:=0)or[l:=v and[v|l|w|8//v*(d:=d*2),(v>0)+(min(t:=sum(g,[]),key=t.count)==v)][c<1]for v,w in zip(s,[0]+t)]for s in zip(*g)][::-1],c-1)
# p=lambda g,c=15,d=8,t=[0]*9:-c*g or p([t:=(l:=0)or[l:=v and[v|l|w|(v<9)*(d:=d*2),sum(g,[]).count(v),(v>0)+(max(sum(g,[]))!=v)][2>>c]for v,w in zip(s,[0]+t)]for s in zip(*g)][::-1],c-1)
