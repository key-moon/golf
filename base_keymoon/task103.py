# best: 29(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, Team JYCDT, lv1.dev, jonas ryno kg583, LogicLynx, HETHAT, ALE-Agent, jacekw Potatoman nauti, santa2024, cg-klogw-sekken, FuunAgent, HashPanda Pooja, natte, kambarakun, HashPanda, Rafael Pooja, JRKXK, import itertools, MasukenSamba, cg-klogw, jailctf merger, Tony Li & Darren Amadeus Martin, HIMAGINE THE FUTURE., adakoda, Yuchen20, ox jam, 2F, biz, duckyluuk, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 30(kabutack), 31(jacekwl), 31(dbdr), 31(Ravi Annaswamy), 31(cg)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
