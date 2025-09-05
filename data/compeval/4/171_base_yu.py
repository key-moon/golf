# best: 54(att) / others: 55(4atj), 56(luke), 57(sisyphus), 61(ovs), 61(mukundan)
# ======================== 54 ========================
# p=lambda g,c=-1:g*c or p([u:=[8]*len(g)]+[*zip(*g)][2:]+[u],c+1)
# p=lambda g:[a:=[8]*len(g[0])]+[[8,*r[2:],8]for r in g[2:]]+[a]
p=lambda g:[a:=[8]*len(g[0]),*[[8,*r[2:],8]for r in g[2:]],a]
# p=lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a