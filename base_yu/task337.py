# best: 43(Code Golf International, jailctf merger, ox jam) / others: 46(cubbus), 46(jacekw Potatoman nauti natte), 46(4atj sisyphus luke Seek mukundan), 46(rucin93), 46(import itertools)
# =================== 43 ==================
# 345678901234567890123456789012345678901234567890
# p=lambda g:[[v^13*(v in(5,8))for v in s]for s in g]
# p=lambda g:[[v^13*(v>v%3>1)for v in s]for s in g]
p=lambda g:eval(str(g).translate({53:56,56:53}))
