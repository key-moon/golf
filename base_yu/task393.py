# best: 63(Potatoman, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, MasukenSamba, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, jacekwl, xsot ovs att joking mewheni, mukundan) / others: 64(Yuchen20), 70(biz), 72(natte), 73(jonas ryno kg583), 73(JRK)
# ============================= 63 ============================
# p=lambda g:[[v]for v,_ in __import__("collections").Counter(sum(g,[])).most_common()[1:]]
# p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
# p=lambda g:[*zip([*sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]])]
p=lambda g:[*zip(sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
# p=lambda g:(u:=sum(g,[]))and[[v]for v in sorted({*u},key=u.count)[2::-1]]
# p=lambda g:[[int(v)]for v in sorted({*str(g)}-{*"[]"},key=str(g).count)[2::-1]]
# p=lambda g:[*map(lambda x:[x],sorted({*(u:=sum(g,[]))},key=u.count)[2::-1])]
