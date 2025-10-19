# best: 37(ShadowPrompt Labs, kabutack, Tony Li, jonas ryno kg583, JRKKX, jacekwl, blob2822, THUNDER THUNDER, jailctf merger, JRK, natte, cubbus, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, HETHAT, Code Golf International, JRKX, ox jam, MasukenSamba, kambarakun, jonas ryno kg583 kabutack, HashPanda, intgrah jimboko awu macaque sammyuri, cg-klogw, Rafael Pooja, HashPanda Pooja, jacekwl Potatoman nauti, cg, biz, cg-klogw-sekken, adakoda, jacekw Potatoman nauti, import itertools, Ravi Annaswamy, jacekw) / others: 38(Potatoman), 39(MKRC), 39(el_presidente), 39(sekken), 39(dbdr)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
