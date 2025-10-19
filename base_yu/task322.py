# best: 48(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, HETHAT, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 49(kabutack), 49(JRKKX), 49(JRKXK), 49(Yuchen20), 49(JRKX)
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
