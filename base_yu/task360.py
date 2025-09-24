# best: 45(jonas ryno kg583 kabutack, jacekwl Potatoman nauti, JRK, JRKX, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, HETHAT, jacekw Potatoman nauti, natte, MasukenSamba, Potatoman, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 52(cubbus), 52(kabutack), 52(cg-klogw), 53(dbdr), 53(Bulmenisaurus)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
