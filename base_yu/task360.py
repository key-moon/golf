# best: 45(Potatoman, ox jam, 4atj sisyphus luke Seek mukundan, JRKX, jacekw Potatoman nauti, MasukenSamba, jailctf merger, intgrah jimboko awu macaque sammyuri, jonas ryno kg583 kabutack, Yuchen20, HETHAT, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK) / others: 52(kabutack), 52(cg-klogw), 53(duckyluuk), 53(dbdr), 53(Bulmenisaurus)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
