# best: 29(duckyluuk, 4atj sisyphus luke Seek mukundan, MasukenSamba, HashPanda, 4atj sisyphus luke Seek, biz, jailctf merger, kg583, intgrah jimboko awu macaque sammyuri, nauti, Yuchen20, HETHAT, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK, mukundan) / others: 30(kabutack), 31(natte), 31(jacekwl Potatoman), 31(dbdr), 31(cg)
# ============ 29 ===========
# 345678901234567890123456789
# p=lambda g:[[7**([*zip(*g)][0]!=[*zip(*g)][2])]]
# p=lambda g:[[7**any(s[0]!=s[2]for s in g)]]
p=lambda g:[[7**any(a!=c for a,_,c in g)]]
