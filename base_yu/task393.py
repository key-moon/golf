# best: 63(jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRKX, 4atj sisyphus luke Seek mukundan, jacekwl, jacekw Potatoman nauti, natte, kabutack, JRKXK, MasukenSamba, Potatoman, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 64(Yuchen20), 66(cg-klogw-sekken), 66(cg-klogw), 70(sekken), 70(2F)
# ============================= 63 ============================
# p=lambda g:[[v]for v,_ in __import__("collections").Counter(sum(g,[])).most_common()[1:]]
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
# p=lambda g:[*zip([*sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]])]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
# p=lambda g:(u:=sum(g,[]))and[[v]for v in sorted({*u},key=u.count)[2::-1]]
# p=lambda g:[[int(v)]for v in sorted({*str(g)}-{*"[]"},key=str(g).count)[2::-1]]
# p=lambda g:[*map(lambda x:[x],sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
