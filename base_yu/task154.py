# best: 96(Ravi Annaswamy) / others: 98(Code Golf International), 98(jailctf merger), 99(4atj sisyphus luke Seek mukundan), 100(ALE-Agent), 100(ox jam)
# ============================================= 96 =============================================
p=lambda g,c=-29,k=3:c*g or p(exec(g[i:=c%15].count(2)//5*2*"g[i-k],g[i+k]=g[i+k],g[i-k];k=2;")or[*zip(*g)],c+1)

# def p(g):
#  for i in range(30):
#   i%=15
#   if g[i].count(2)>4:
#    k=3
#    exec("g[i-k],g[i+k]=g[i+k],g[i-k];k=2;"*2)
# #    g[i-3],g[i+3]=g[i+3],g[i-3]
# #    g[i-2],g[i+2]=g[i+2],g[i-2]
# #    g[i-3:i+4]=g[i-3:i+4][::-1]
# #    g[i-1:i+2]=g[i-1:i+2][::-1]
#   *g,=zip(*g)
#  return g

# def p(g):
#  for i in range(30):
#   i%=15
#   if g[i].count(2)>4:
#    g[i-3:i-1],g[i+2:i+4]=g[i+3:i+1:-1],g[i-3:i-1][::-1]
#   *g,=zip(*g)
#  return g
