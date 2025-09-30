# best: 37(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, blob2822, JRKX, 4atj sisyphus luke Seek mukundan, jacekw, jacekwl, jonas ryno kg583, HETHAT, jacekw Potatoman nauti, cg-klogw-sekken, HashPanda Pooja, natte, cg, HashPanda, Rafael Pooja, kabutack, MasukenSamba, cg-klogw, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 38(Potatoman), 39(open source), 39(Ali), 39(Afordancja), 39(dbdr)
# ================ 37 ===============
# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
