# best: 148(xsot ovs att joking mewheni) / others: 151(4atj sisyphus luke Seek), 153(natte), 161(jailctf merger), 172(kg583), 213(MasukenSamba)
# ====================================================================== 148 =======================================================================
def p(g):
 *o,=eval("[0]*4,"*4)
 for _ in range(4):
  for i in range(12):
   for j in range(12):
    if g[i][j]==g[i+1][j]==g[i][j+1]>0:
     o[0][0]=o[0][1]=o[1][0]=g[i][j]
  *g,=zip(*g[::-1])
  *o,=map(list,zip(*o[::-1]))
 return o
