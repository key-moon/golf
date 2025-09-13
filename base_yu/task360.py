# best: 45(Potatoman, 4atj sisyphus luke Seek mukundan, MasukenSamba, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK) / others: 48(Yuchen20), 52(kabutack), 53(duckyluuk), 53(dbdr), 53(Bulmenisaurus)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
