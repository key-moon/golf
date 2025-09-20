# best: 218(jailctf merger) / others: 219(4atj sisyphus luke Seek mukundan), 222(HashPanda Pooja), 222(garrymoss), 222(Rafael Pooja), 222(natte)
def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   for y in range(len(g)-2):
    for x in range(len(g[0])-2):
     for k in range(9*(sum(a:=[g[i+k//3][k%3+j] for k in range(9)])>a[4]>0and a==a[::-1]and(sum(g[y+k//3][k%3+x]==g[i+k//3][k%3+j]for k in range(9))>7or a[4]==g[y+1][1+x]))):
      g[y+k//3][k%3+x]=g[i+k//3][k%3+j]
 return g
