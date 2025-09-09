# best: 63(Potatoman, 4atj sisyphus luke Seek mukundan, MasukenSamba, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni) / others: 64(Yuchen20), 66(kdmitrie), 71(natte), 72(jonas ryno kg583), 72(JRK)
# ============================= 63 ============================
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]


