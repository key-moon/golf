# best: 63(ShadowPrompt Labs, kabutack, JRKKX, jacekwl, jailctf merger, natte, JRKXK, 4atj sisyphus luke Seek mukundan, Potatoman, jacekw Potatoman nauti natte, JRKX, ox jam, MasukenSamba, intgrah jimboko awu macaque sammyuri, jacekwl Potatoman nauti, adakoda, jacekw Potatoman nauti, import itertools) / others: 64(Yuchen20), 66(cg-klogw), 66(cg-klogw-sekken), 68(Tony Li), 70(sekken)
# ============================= 63 ============================
# p=lambda g:[[v]for v,_ in __import__("collections").Counter(sum(g,[])).most_common()[1:]]
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
# p=lambda g:[*zip([*sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]])]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
# p=lambda g:(u:=sum(g,[]))and[[v]for v in sorted({*u},key=u.count)[2::-1]]
# p=lambda g:[[int(v)]for v in sorted({*str(g)}-{*"[]"},key=str(g).count)[2::-1]]
# p=lambda g:[*map(lambda x:[x],sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
