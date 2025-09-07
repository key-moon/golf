# best: 63(mukundan, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, Potatoman, xsot ovs att joking mewheni, HETHAT, 4atj sisyphus luke Seek, jailctf merger, MasukenSamba, intgrah jimboko awu macaque sammyuri, jacekwl) / others: 64(Yuchen20), 66(kdmitrie), 71(natte), 72(kg583), 72(jonas ryno kg583)
# ============================= 63 ============================
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
