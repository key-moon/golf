# best: 58(joking+MWI, mukundan, luke, joking, xsot, ovs, sisyphus) / others: 59(nauti), 60(kabutack), 70(Bulmenisaurus), 70(dbdr), 71(MasukenSamba)
# lambda g:[[*r]for r in zip(*g[:3])]!=g[:3]and g[:3]or p(g[3:])
# lambda g:[*map(list,zip(*g[:3]))]!=g[:3]and g[:3]or p(g[3:])
# lambda g:(a:=g[:3])!=[*map(list,zip(*a))]and a or p(g[3:])
# lambda g:a if(a:=g[:3])!=[*map(list,zip(*a))]else p(g[3:])
# ========================== 58 ==========================
p=lambda g:(a:=g[:3])!=[*map(list,zip(*a))]and a or p(g[3:])