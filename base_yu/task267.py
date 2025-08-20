# best: 48(luke) / others: 50(4atj), 51(mukundan), 53(joking), 56(nauti), 56(kg583)
# ===================== 48 =====================
# p=lambda g:[[v and g[6][0]for v in s]for s in g[:6]+g[:1]]
p=lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# p=lambda g:[[(v>0)*g[6][0]for v in s]for s in g[:6]+g[:1]]
