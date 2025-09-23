# best: 48(natte, ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT) / others: 49(JRKX), 49(kabutack), 49(Yuchen20), 51(cubbus), 51(jacekw Potatoman nauti)
# ===================== 48 =====================
# p=lambda g:[*map(list,zip(*[[max(s[:i+1])for i in range(3)] for s in zip(*g)]))]
# p=lambda g:[[max(v)for v in zip(*g[:i])]for i in(1,2,3)]
p=lambda g:[[*map(max,zip(*g[:i]))]for i in(1,2,3)]
# def p(g):
#  for a,b in zip(g[1:],g):
#   for i in 0,1,2:a[i]|=b[i]
#  return g
# def p(g):
#  for i in 0,1:
#   for j in 0,1,2:g[i+1][j]|=g[i][j]
#  return g
