# best: 45(kg583, mukundan, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, Potatoman, xsot ovs att joking mewheni, jonas ryno kg583, HETHAT, 4atj sisyphus luke Seek, jailctf merger, JRK, MasukenSamba, intgrah jimboko awu macaque sammyuri) / others: 52(Yuchen20), 52(kabutack), 52(nauti), 53(Bulmenisaurus), 53(duckyluuk)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
