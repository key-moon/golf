# best: 126(lv1.dev) / others: 130(ox jam), 131(ALE-Agent), 134(jailctf merger), 135(Code Golf International), 136(FuunAgent)
# =========================================================== 126 ============================================================
def p(g):
 n=len(g[0])
 R=range(n*n)
 f=8in max(g[:n])
#  if n>5:
#   return[*zip(*p([*zip(*g)]))]
#  return[[g[i%n+n-f*n][j%n]and g[i//n+f*n][j//n]for j in R]for i in R]
 return n<6and [[g[i%n+n-f*n][j%n]and g[i//n+f*n][j//n]for j in R]for i in R]or[*zip(*p([*zip(*g)]))]
#  return[[g[i+f*n][j]and g[y+n-f*n][x]for x in R for j in R]for y in R for i in R]
