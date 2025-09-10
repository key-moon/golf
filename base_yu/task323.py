# best: 102(jailctf merger) / others: 106(4atj sisyphus luke Seek mukundan), 125(xsot ovs att joking mewheni), 150(jacekwl), 150(jacekwl Potatoman nauti), 154(natte)
# =============================================== 102 ================================================
# def p(g,R=range(13)):
#  y,x=divmod(sum(g,[]).index(8),13)
#  return[[g[i][j]or(abs(i+j-y-x-(1|-(i<y)))<2*(i!=y)-(i-y)%2)*5for j in R]for i in R]

# p=lambda g,R=range(13):[[g[i][j]+(abs((d:=i-(k:=sum(g,[]).index(8))//13)+j-k%13-(1|-(d<0)))<2*(d!=0)-d%2)*5for j in R]for i in R]
p=lambda g,R=range(13):[[g[i][j]+(abs((d:=i-(k:=sum(g,[]).index(8))//13)+j-k%13-(d//7|1))<2*(d!=0)-d%2)*5for j in R]for i in R]

# def p(g,R=range(13)):
#  k=sum(g,[]).index(8)
#  return[[g[i][j]or(abs((d:=i-k//13)+j-k%13-(1|-(d<0)))<2*(d!=0)-d%2)*5for j in R]for i in R]

# def p(g,R=range(13)):
#  k=sum(g,[]).index(8)
#  y=k//13
#  x=k%13
#  return[[g[i][j]or(abs(i+j-y-x-(1|-(i<y)))<2*(i!=y)-(i-y)%2)*5for j in R]for i in R]


# def p(g):
#  for _ in 0,1:
#   i=sum(g,[]).index(8)
#   for d in(13,13,-1,-1)*99:
#    i+=d
#    if i>168 or i%13-d>12:break
#    g[i//13][i%13]=5
#   g=[s[::-1]for s in g[::-1]]
#  return g
