# best: 217(jailctf merger) / others: 219(4atj sisyphus luke Seek mukundan), 220(kambarakun), 222(sekken), 222(JRKKX), 222(blob2822)
def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   for y in range(len(g)-2):
    for x in range(len(g[0])-2):
     for k in range(9*(sum(a:=[g[i+k//3][k%3+j] for k in range(9)])>a[4]>0and a==a[::-1]and(sum(g[y+k//3][k%3+x]==g[i+k//3][k%3+j]for k in range(9))>7or a[4]==g[y+1][1+x]))):
      g[y+k//3][k%3+x]=g[i+k//3][k%3+j]
 return g
