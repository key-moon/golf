# best: 58(jonas ryno kg583 kabutack, jacekw Potatoman nauti natte, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, jacekw Potatoman nauti, natte, JRKXK, import itertools, MasukenSamba, jailctf merger, ox jam, biz, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 59(jacekwl Potatoman nauti), 59(Yuchen20), 60(kabutack), 61(HETHAT), 67(Krige)
# lambda g:[[*r]for r in zip(*g[:3])]!=g[:3]and g[:3]or p(g[3:])
# lambda g:[*map(list,zip(*g[:3]))]!=g[:3]and g[:3]or p(g[3:])
# lambda g:p(g[3:])if[*map(list,zip(*g[:3]))]==g[:3]else g[:3]
# lambda g:(a:=g[:3])!=[*map(list,zip(*a))]and a or p(g[3:])
# lambda g:a if(a:=g[:3])!=[*map(list,zip(*a))]else p(g[3:])
# ========================== 58 ==========================
# p=lambda g:p(g[3:])if(a:=g[:3])==[*map(list,zip(*a))]else a
p=lambda g:(a:=g[:3])*(a!=[*map(list,zip(*a))])or p(g[3:])
