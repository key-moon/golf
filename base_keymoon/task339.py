# best: 37(natte, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, MasukenSamba, HashPanda, 4atj sisyphus luke Seek, jacekw, kabutack, cg, jailctf merger, kg583, intgrah jimboko awu macaque sammyuri, nauti, Yuchen20, HETHAT, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK, mukundan) / others: 38(Potatoman), 39(el_presidente), 39(J&R), 39(kdmitrie), 39(scpchicken)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
