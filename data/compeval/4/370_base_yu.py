# def p(g):
#  h,w=len(g),len(g[0])
#  G=sum(g,[])
#  _,k,c=min((G.count(v),i,v)for i,v in enumerate(G))
# #  for i,v in enumerate(G):if G.count(v)==1:k,c=i,v
#  _,l=max((abs(i-k)+abs(i%w-k%w)*2,i)for i,v in enumerate(G)if v<1)
#  for I in range(h*w*9):
#   if g[i:=I//9//w][j:=I//9%w]<1:
#    y=i-~(I%9)*(k//w-l//w)
#    x=j-~(I%9)*(k%w-l%w)
#    if-1<y<h and-1<x<w:g[y][x]=c
#  return g

def p(g):
 h,w=len(g),len(g[0])
 G=sum(g,[])
 _,k,c=min((G.count(v),i,v)for i,v in enumerate(G))
#  for i,v in enumerate(G):if G.count(v)==1:k,c=i,v
 _,l=max((abs(i-k)+abs(i%w-k%w)*2,i)for i,v in enumerate(G)if v<1)
 for i in range(h):
  for j in range(w):
   for t in range(9*(g[i][j]<1)):
    if-1<(y:=i-~t*(k//w-l//w))<h and-1<(x:=j-~t*(k%w-l%w))<w:g[y][x]=c
 return g

# def p(g):
#  h,w=len(g),len(g[0])
#  G=sum(g,[])
#  _,k,c=min((G.count(v),i,v)for i,v in enumerate(G))
# #  for i,v in enumerate(G):if G.count(v)==1:k,c=i,v
#  _,l=max((abs(i-k)+abs(i%w-k%w)*2,i)for i,v in enumerate(G)if v<1)
#  for i in range(h):
#   for j in range(w):
#    for t in range(9*(g[i][j]<1)):
#     if-1<(y:=i-~t*(k//w-l//w))<h and-1<(x:=j-~t*(k%w-l%w))<w:g[y][x]=c
#  return g