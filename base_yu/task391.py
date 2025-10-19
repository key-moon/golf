# best: 63(jacekwl, jailctf merger, natte, 4atj sisyphus luke Seek mukundan, Potatoman, jacekw Potatoman nauti natte, HETHAT, Code Golf International, ox jam, MasukenSamba, intgrah jimboko awu macaque sammyuri, jacekwl Potatoman nauti, adakoda, jacekw Potatoman nauti, import itertools) / others: 64(Yuchen20), 66(ShadowPrompt Labs), 66(JRKKX), 66(JRKXK), 66(kdmitrie)
# ============================= 63 ============================
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
