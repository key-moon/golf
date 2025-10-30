# best: 65(jacekwl Potatoman nauti, jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, jacekwl, jacekw Potatoman nauti, cg-klogw-sekken, natte, import itertools, MasukenSamba, cg-klogw, jailctf merger, HIMAGINE THE FUTURE., Yuchen20, ox jam, THUNDER THUNDER, biz, duckyluuk) / others: 66(JRKX), 66(HETHAT), 66(JRKXK), 66(adakoda), 66(JRKKX)
# ============================== 65 =============================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
