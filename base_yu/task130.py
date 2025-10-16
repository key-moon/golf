# best: 65(jacekwl, THUNDER THUNDER, jailctf merger, natte, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, duckyluuk, ox jam, MasukenSamba, intgrah jimboko awu macaque sammyuri, cg-klogw, jacekwl Potatoman nauti, biz, cg-klogw-sekken, jacekw Potatoman nauti, import itertools) / others: 66(JRKKX), 66(JRKXK), 66(HETHAT), 66(JRKX), 66(adakoda)
# ============================== 65 =============================
# p=lambda g:[[sum({*s[i*3:i*3+3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[sum({*s[i*3:][:3]}-{5})for i in range(3)]for s in g[1::3]]
# p=lambda g:[[*map(lambda f:sum({*f}-{5}),zip(*[iter(s)]*3))]for s in g[1::3]]
# p=lambda g:[[sum({*f}-{5})for f in zip(*[iter(s)]*3)]for s in g[1::3]]
p=lambda g:[[sum({*s[i:i+3]}-{5})for i in(0,3,6)]for s in g[::3]]
