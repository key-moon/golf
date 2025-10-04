# best: 112(jailctf merger) / others: 116(4atj sisyphus luke Seek mukundan), 119(ox jam), 128(jacekw Potatoman nauti natte), 128(jacekw Potatoman nauti), 137(Yuchen20)
# ==================================================== 112 =====================================================
# lambda g,c=-3,x=0:c*[[(d:=min(u:=sum(g,[]),key=u.count))*(y==d)for y in s]for s in g]or[[[(x>0)*2,x:=y][x>0]for y in s]for s in zip(*p(g,c+1)[::-1])]
# p=lambda g,c=-3:c*[[(d:=min(u:=sum(g,[]),key=u.count))*(y==d)for y in s]for s in g]or[[[(c>0)*2,c:=y][y>0]for y in s]for s in zip(*p(g,c+1)[::-1])]
# p=lambda g,c=-3,l=0:c*[[(d:=min(u:=sum(g,[]),key=u.count))*(y==d)for y in s]for s in g]or[[[(l>0)*2,l:=y][y>0]for y in s]for s in zip(*p(g,c+1)[::-1])]
p=lambda g,c=-3,l=0:c*g or[[[(l>0)*2,l:=y*(y==min(u:=sum(g,[]),key=u.count)or c<0)][l>0]for y in s]for s in zip(*p(g,c+1)[::-1])]


# def p(g):
#  g = [[(c:=min(u:=sum(g,[]),key=u.count))*(y==c)for y in s]for s in g]
#  for _ in range(4):
#   x=0
#   g = [[[(x>0)*2,x:=y][x>0]for y in s]for s in zip(*g[::-1])]
#  return g
