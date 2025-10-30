# best: 230(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, jailctf merger) / others: 249(HIMAGINE THE FUTURE.), 256(JRKXK), 256(kdmitrie), 256(JRKKX), 265(ShadowPrompt Labs)
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
 _,k,c=min((sum(g,[]).count(v),i,v)for i,v in enumerate(sum(g,[])))
#  for i,v in enumerate(G):if G.count(v)==1:k,c=i,v
 _,l=max((abs(i-k)+abs(i%len(g[0])-k%len(g[0]))*2,i)for i,v in enumerate(sum(g,[]))if v<1)
 for i in range(len(g)):
  for j in range(len(g[0])):
   for t in range(9):
    if g[i][j]<1 and i-~t*(k//len(g[0])-l//len(g[0])) in range(len(g)) and j-~t*(k%len(g[0])-l%len(g[0])) in range(len(g[0])):g[i-~t*(k//len(g[0])-l//len(g[0]))][j-~t*(k%len(g[0])-l%len(g[0]))]=c
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
