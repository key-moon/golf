# best: 253(ox jam) / others: 255(jailctf merger), 255(HIMAGINE THE FUTURE.), 255(THUNDER THUNDER), 270(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 274(import itertools)
def p(g):
 a,*_,b,c=sorted({*sum(g,[])},key=lambda c:(sum(g,[]).count(c),sum(g,[])[::-1].index(c)+sum(g,[]).index(c)))
 s=sum(g,[]).index(b^c)+1
 for i in range(len(g)):
  for j in range(len(g)):
   for y in range(len(g)):
    for x in range(len(g)):
     for k in (-s,0,s):
      for l in (-s,0,s):
       if g[i][j]==g[y][x]==a and -1<i+k<len(g)>j+l>-1<y+k<len(g)>x+l>-1:
        g[y+k][x+l]|=g[i+k][j+l]
 return g
