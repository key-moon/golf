# best: 29(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, JRKX, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, HETHAT, jacekw Potatoman nauti, cg-klogw-sekken, HashPanda Pooja, natte, HashPanda, Rafael Pooja, JRKXK, MasukenSamba, cg-klogw, jailctf merger, Yuchen20, ox jam, 2F, biz, duckyluuk, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 30(kabutack), 31(jacekwl), 31(dbdr), 31(cg), 31(Tony Li)
# ============ 29 ===========
# 345678901234567890123456789
# p=lambda g:[[7**([*zip(*g)][0]!=[*zip(*g)][2])]]
# p=lambda g:[[7**any(s[0]!=s[2]for s in g)]]
p=lambda g:[[7**any(a!=c for a,_,c in g)]]
