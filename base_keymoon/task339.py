# best: 37(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, jacekw, jacekwl, jonas ryno kg583, ShadowPrompt Labs, HETHAT, jacekw Potatoman nauti, cg-klogw-sekken, HashPanda Pooja, Ravi Annaswamy, natte, cg, kambarakun, HashPanda, Rafael Pooja, kabutack, JRKXK, import itertools, MasukenSamba, cg-klogw, Tony Li, jailctf merger, Tony Li & Darren Amadeus Martin, adakoda, Yuchen20, ox jam, THUNDER THUNDER, biz, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 38(Potatoman), 39(open source), 39(Ali), 39(Krige), 39(Afordancja)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
