# best: 96(sisyphus) / others: 104(ovs), 109(mukundan), 109(Seek64), 109(biz), 112(joking+MWI)
# ============================================= 96 =============================================
# E=lambda g:[*filter(max,zip(*g))]
# def p(g):
#  p=E(E(g))
#  return[[x&y for x in s for y in t]for s in p for t in p]
# p=lambda g:(u:=[[max(max(s[j::3])for s in g[i::3])for j in range(3)]for i in range(3)])and[[x&y for x in s for y in t]for s in u for t in u]
# lambda g,E=lambda g:filter(max,zip(*g)):[[x&y for x in s for y in t]for s in E(E(g))for t in E(E(g))]
p=lambda g,c=-1:c*[[x&y for x in s for y in t]for s in g for t in g]or[*zip(*filter(max,p(g,c+1)))]
