# best: 29(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, Team JYCDT, lv1.dev, jonas ryno kg583, LogicLynx, HETHAT, ALE-Agent, jacekw Potatoman nauti, santa2024, cg-klogw-sekken, FuunAgent, HashPanda Pooja, Ravi Annaswamy, natte, kambarakun, HashPanda, Rafael Pooja, JRKXK, import itertools, MasukenSamba, cg-klogw, jailctf merger, Tony Li & Darren Amadeus Martin, HIMAGINE THE FUTURE., adakoda, Yuchen20, ox jam, 2F, biz, duckyluuk, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 30(ShadowPrompt Labs), 30(kabutack), 31(jacekwl), 31(dbdr), 31(cg)
# ============ 29 ===========
# 345678901234567890123456789
# p=lambda g:[[7**([*zip(*g)][0]!=[*zip(*g)][2])]]
# p=lambda g:[[7**any(s[0]!=s[2]for s in g)]]
p=lambda g:[[7**any(a!=c for a,_,c in g)]]
