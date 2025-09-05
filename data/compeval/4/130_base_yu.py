# best: 65(ovs, luke, mukundan, 4atj, luke/sisyphus/Seek, joking+MWI, joking/MWI, joking, att, xsot, duckyluuk, sisyphus) / others: 66(nauti), 68(kabutack), 74(MasukenSamba), 90(Seek64), 91(natte)
# ============================== 65 =============================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
