# best: 61(Code Golf International) / others: 65(jacekwl Potatoman nauti), 65(jacekw Potatoman nauti natte), 65(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 65(4atj sisyphus luke Seek mukundan), 65(lv1.dev)
# ============================ 61 ===========================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
