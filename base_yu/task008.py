# best: 94(ovs, xsot ovs) / others: 95(4atj sisyphus luke Seek), 96(mukundan), 97(att), 98(4atj), 106(joking MeWhenI)
# ============================================ 94 ============================================
S=sorted;p=lambda g:2in(b:=max(g,key=sum))and[*zip(*p([*zip(*g)]))]or S(g[:(i:=g.index(b))],key=max)+S(g[:i-1:-1],key=max)[::-1]
