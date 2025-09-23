# best: 63(natte, Potatoman, ox jam, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti, MasukenSamba, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni) / others: 64(Yuchen20), 66(kdmitrie), 66(cg-klogw), 70(sekken), 72(JRKX)
# ============================= 63 ============================
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
