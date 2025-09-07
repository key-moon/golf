# best: 37(kg583, mukundan, jacekw, 4atj sisyphus luke Seek mukundan, cg, HashPanda, jacekwl Potatoman, xsot ovs att joking mewheni, jonas ryno kg583, Yuchen20, HETHAT, 4atj sisyphus luke Seek, kabutack, jailctf merger, JRK, nauti, MasukenSamba, natte, intgrah jimboko awu macaque sammyuri, jacekwl) / others: 38(Potatoman), 39(KN), 39(adakoda), 39(kdmitrie), 39(el_presidente)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
