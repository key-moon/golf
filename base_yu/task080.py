# best: 253(ox jam) / others: 255(jailctf merger), 255(HIMAGINE THE FUTURE.), 255(THUNDER THUNDER), 259(import itertools), 270(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
def p(g):
 a,*_,b,c=sorted({*sum(g,[])},key=lambda c:(sum(g,[]).count(c),sum(g,[])[::-1].index(c)+sum(g,[]).index(c)))
 s=sum(g,[]).index(b^c)+1
 for i in range(len(g)):
  for j in range(len(g)):
   for y in range(len(g)):
    for x in range(len(g)):
     for k in (-s,0,s):
      for l in (-s,0,s):
       if g[i][j]==g[y][x]==a and i+k in range(len(g)) and x+l in range(len(g)) and y+k in range(len(g)) and j+l in range(len(g)):
        g[y+k][x+l]|=g[i+k][j+l]
 return g
