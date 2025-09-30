# best: 63(jacekwl Potatoman nauti, jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, jacekwl, HETHAT, jacekw Potatoman nauti, natte, MasukenSamba, Potatoman, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(Yuchen20), 66(cg-klogw-sekken), 66(cg-klogw), 66(kdmitrie), 70(sekken)
# ============================= 63 ============================
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
