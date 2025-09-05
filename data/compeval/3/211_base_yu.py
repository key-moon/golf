# best: 48(ovs, luke, 4atj, Seek64, MeWhenI, sisyphus) / others: 49(HETHAT), 49(nauti), 49(natte), 49(MasukenSamba), 49(att)
# ===================== 48 =====================
# p=lambda g:[g[i][::-1]+g[i]for i in(2,1,0,0,1,2,2,1,0)]
# p=lambda g:[s[::-1]+s for s in g[::-1]+g+g[::-1]]
# p=lambda g:[s[::-1]+s for s in((g[::-1]+g)*2)[:9]]
p=lambda g:[s[::-1]+s for s in(g[::-1]+g)*2][:9]
# p=lambda g:(u:=g[::-1])and[s[::-1]+s for s in u+g+u]
