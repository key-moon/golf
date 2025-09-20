# best: 37(natte, ox jam, 4atj sisyphus luke Seek mukundan, JRKX, Rafael Pooja, MasukenSamba, HashPanda, jacekw, kabutack, cg, jailctf merger, intgrah jimboko awu macaque sammyuri, HashPanda Pooja, jonas ryno kg583 kabutack, Yuchen20, HETHAT, cg-klogw, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK) / others: 38(Potatoman), 39(el_presidente), 39(azakhtyamov), 39(J&R), 39(kdmitrie)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
