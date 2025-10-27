# best: 132(HIMAGINE THE FUTURE.) / others: 134(Code Golf International), 134(4atj sisyphus luke Seek mukundan), 135(ox jam), 136(import itertools), 136(Tony Li)
# ============================================================== 132 ===============================================================
def p(g):
 for i in range(10):
  for j in range(10):
   s=[(i,j)]
   for y,x in s:
    for k in range(4):
     Y=y+7%~k+1
     X=x+k+2%~k*2
     if -1<Y<10>X>-1 and g[Y][X] and (Y,X) not in s:
      s.append((Y,X))
   if g[i][j]:
    g[i][j]=(len(s)==6)+1
 return g

# def p(g,y=0,x=0,c=0):
#  if c>0:
#   g[y][x]=c
#   return sum(-1<(Y:=y+7%~k+1)<10>(X:=x+k+2%~k*2)>-1 and g[Y][X]==c*5%9 and p(g,Y,X,c)for k in range(4))+1
#  [g[i:=I//10][j:=I%10]==5 and p(g,i,j,1)==6 and p(g,i,j,2)for I in range(100)]
#  return g

# def p(g,y=0,x=0,c=0):
#  if c>0:
#   d=1
#   g[y][x]=c
#   for k in range(4):
#    X=x+k+2%~k*2
#    Y=y+7%~k+1
#    d+=-1<Y<10>X>-1 and g[Y][X]==c*5%9 and p(g,Y,X,c)
#   return d
#  for i in range(10):
#   for j in range(10):
#    if g[i][j]==5 and p(g,i,j,1)==6:
#     p(g,i,j,2)
#  return g
