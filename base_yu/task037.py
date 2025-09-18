# best: 105(4atj sisyphus luke Seek mukundan) / others: 108(jailctf merger), 109(ox jam), 109(xsot ovs att joking mewheni), 136(jonas ryno kg583), 144(MasukenSamba)
# ================================================= 105 =================================================


# p=lambda g,c=-3,z=[0]*10,R=range:c*g or p([[sum({(g[~k]+z)[i+j-k]for k in R(j+1)}&{(g[~k]+z)[i+j-k]for k in R(j,10)})for j in R(10)]for i in R(10)],c+1)
# p=lambda g,c=-1,z=[0]*9,R=range:c*g or p([[sum({(g[~k]+z)[i+j-k]for k in R(i+1)}&{(g[~k]+z)[i+j-k]for k in R(i,10)})for j in R(10)]for i in R(10)],c+1)
p=lambda g,c=-1,z=[0]*9,R=range:c*g or p([[sum((f:=lambda r:{(g[~k]+z)[i+j-k]for k in r})(R(i+1))&f(R(i,10)))for j in R(10)]for i in R(10)],c+1)

# def p(g,z=[0]*10,R=range):
#  for _ in range(4):
#   g=[[sum({(g[~k]+z)[i+j-k]for k in R(j+1)}&{(g[~k]+z)[i+j-k]for k in R(j,10)})for j in R(10)]for i in R(10)]
#  return g
