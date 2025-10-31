# best: 201(jailctf merger) / others: 204(ox jam), 207(Code Golf International), 208(HIMAGINE THE FUTURE.), 215(lv1.dev), 219(4atj sisyphus luke Seek mukundan)
def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   for y in range(len(g)-2):
    for x in range(len(g[0])-2):
     for k in range(9*(sum(a:=[g[i+k//3][k%3+j] for k in range(9)])>a[4]>0<(sum(g[y+k//3][k%3+x]==g[i+k//3][k%3+j]for k in range(9))>7or a[4]==g[y+1][1+x])and a==a[::-1])):
      g[y+k//3][k%3+x]=g[i+k//3][k%3+j]
 return g
