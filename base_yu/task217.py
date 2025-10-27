# best: 95(jailctf merger, ox jam) / others: 96(Code Golf International), 96(4atj sisyphus luke Seek mukundan), 99(HIMAGINE THE FUTURE.), 99(intgrah jimboko awu macaque sammyuri), 101(import itertools)
# ============================================= 95 ============================================
# E=lambda g:[*filter(max,zip(*g))]
# def p(g):
#  p=E(E(g))
#  return[[x&y for x in s for y in t]for s in p for t in p]
# p=lambda g:(u:=[[max(max(s[j::3])for s in g[i::3])for j in range(3)]for i in range(3)])and[[x&y for x in s for y in t]for s in u for t in u]
# lambda g,E=lambda g:filter(max,zip(*g)):[[x&y for x in s for y in t]for s in E(E(g))for t in E(E(g))]
p=lambda g,c=-1:c*[[x&y for x in s for y in t]for s in g for t in g]or[*zip(*filter(max,p(g,c+1)))]
