# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 109(ox jam), 111(import itertools), 117(intgrah jimboko awu macaque sammyuri), 123(adakoda), 124(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================================= 105 =================================================


# p=lambda g,c=-3,z=[0]*10,R=range:c*g or p([[sum({(g[~k]+z)[i+j-k]for k in R(j+1)}&{(g[~k]+z)[i+j-k]for k in R(j,10)})for j in R(10)]for i in R(10)],c+1)
# p=lambda g,c=-1,z=[0]*9,R=range:c*g or p([[sum({(g[~k]+z)[i+j-k]for k in R(i+1)}&{(g[~k]+z)[i+j-k]for k in R(i,10)})for j in R(10)]for i in R(10)],c+1)
p=lambda g,c=-1,z=[0]*9,R=range:c*g or p([[sum((f:=lambda r:{(g[~k]+z)[i+j-k]for k in r})(R(i+1))&f(R(i,10)))for j in R(10)]for i in R(10)],c+1)

# def p(g,z=[0]*10,R=range):
#  for _ in range(4):
#   g=[[sum({(g[~k]+z)[i+j-k]for k in R(j+1)}&{(g[~k]+z)[i+j-k]for k in R(j,10)})for j in R(10)]for i in R(10)]
#  return g
