# best: 116(4atj sisyphus luke Seek mukundan, mukundan) / others: 117(4atj sisyphus luke Seek), 117(jailctf merger), 119(xsot ovs att joking mewheni), 142(jonas ryno kg583), 144(kg583)
# ====================================================== 116 =======================================================

p=lambda g,c=-3,x=0:c*[[(d:=min(u:=sum(g,[]),key=u.count))*(y==d)for y in s]for s in g]or[[[(x>0)*2,x:=y][x>0]for y in s]for s in zip(*p(g,c+1)[::-1])]

# def p(g):
#  g = [[(c:=min(u:=sum(g,[]),key=u.count))*(y==c)for y in s]for s in g]
#  for _ in range(4):
#   x=0
#   g = [[[(x>0)*2,x:=y][x>0]for y in s]for s in zip(*g[::-1])]
#  return g
