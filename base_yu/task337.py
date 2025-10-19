# best: 46(jailctf merger, cubbus, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, rucin93, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 48(ShadowPrompt Labs), 48(kabutack), 48(jonas ryno kg583), 48(JRKKX), 48(jacekwl)
# ==================== 46 ====================
# 345678901234567890123456789012345678901234567890
# p=lambda g:[[v^13*(v in(5,8))for v in s]for s in g]
# p=lambda g:[[v^13*(v>v%3>1)for v in s]for s in g]
p=lambda g:eval(str(g).translate({53:56,56:53}))
