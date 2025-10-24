# best: 108(import itertools, jailctf merger, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 110(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 110(MasukenSamba), 111(Tony Li & Darren Amadeus Martin), 113(ox jam), 116(cg-klogw-sekken)
# ================================================== 108 ===================================================
# lambda g,E=enumerate:[[v*(1<str([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3]).count(str(v)))for j,v in E(r)]for i,r in E(g)]
p=lambda g,E=enumerate:[[v*(v<sum(sum([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3],())))for j,v in E(r)]for i,r in E(g)]
