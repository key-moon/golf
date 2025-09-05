# best: 46(4atj sisyphus luke Seek, rucin93, jailctf merger, xsot ovs att joking mewheni, mukundan) / others: 48(natte), 48(HETHAT), 48(HashPanda), 48(MasukenSamba), 48(kabutack)
# ==================== 46 ====================
# 345678901234567890123456789012345678901234567890
# p=lambda g:[[v^13*(v in(5,8))for v in s]for s in g]
# p=lambda g:[[v^13*(v>v%3>1)for v in s]for s in g]
p=lambda g:eval(str(g).translate({53:56,56:53}))
