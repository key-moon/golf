def p(g):
 (a,_),(b,_),(c,_)=__import__("collections").Counter(sum(g,[])).most_common()
 h,w=len(g),len(g[0])
 for I in range(h*w):
  if g[i:=I//w][j:=I%w]==c:
   u=0
   for k in range(9):
    if-1<(y:=i+k//3-1)<h and-1<(x:=j+k%3-1)<w and g[y][x]!=a:
     u+=k%2+1
     u|=(k%6==1)*16|(k in(3,5))*32
   g[i][j]=[a,b][u>52]
 return g


# def p(g):
#  (a,_),(b,_),(c,_)=__import__("collections").Counter(sum(g,[])).most_common()
#  h,w=len(g),len(g[0])
#  for i in range(h):
#   for j in range(w):
#    if g[i][j]==c:
#     u=s=t=0
#     for k in range(9):
#      y=i+k//3-1
#      x=j+k%3-1
#      if-1<y<h and-1<x<w and g[y][x]!=a:
#       u+=k%2+1
#       s|=k%6==1
#       t|=k in (3,5)
#     g[i][j]=[a,b][(u>4)*s*t]
#  return g
