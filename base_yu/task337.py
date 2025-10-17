# best: 46(cubbus, jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, rucin93, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 48(jonas ryno kg583 kabutack), 48(jacekwl Potatoman nauti), 48(JRK), 48(JRKX), 48(jacekw)
# ==================== 46 ====================
# 345678901234567890123456789012345678901234567890
# p=lambda g:[[v^13*(v in(5,8))for v in s]for s in g]
# p=lambda g:[[v^13*(v>v%3>1)for v in s]for s in g]
p=lambda g:eval(str(g).translate({53:56,56:53}))
