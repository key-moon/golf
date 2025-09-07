# best: 136(xsot ovs att joking mewheni) / others: 156(4atj sisyphus luke Seek mukundan), 156(mukundan), 174(jailctf merger), 179(natte), 184(Yuchen20)
# ================================================================ 136 =================================================================
def p(g):
 n=len(g[0])
 R=range(n*n)
 f=8in max(g[:n])
#  if n>5:
#   return[*zip(*p([*zip(*g)]))]
#  return[[g[i%n+n-f*n][j%n]and g[i//n+f*n][j//n]for j in R]for i in R]
 return n<6and [[g[i%n+n-f*n][j%n]and g[i//n+f*n][j//n]for j in R]for i in R]or[*zip(*p([*zip(*g)]))]
#  return[[g[i+f*n][j]and g[y+n-f*n][x]for x in R for j in R]for y in R for i in R]
