# best: 37(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, jacekw, jacekwl, jonas ryno kg583, LogicLynx, HETHAT, ALE-Agent, jacekw Potatoman nauti, santa2024, cg-klogw-sekken, FuunAgent, HashPanda Pooja, Ravi Annaswamy, natte, cg, kambarakun, HashPanda, Rafael Pooja, kabutack, JRKXK, import itertools, MasukenSamba, cg-klogw, Tony Li, jailctf merger, Tony Li & Darren Amadeus Martin, HIMAGINE THE FUTURE., adakoda, Yuchen20, ox jam, THUNDER THUNDER, biz, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 38(Potatoman), 39(open source), 39(Ali), 39(Krige), 39(Afordancja)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
