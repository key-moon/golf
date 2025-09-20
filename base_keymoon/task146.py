# best: 58(ox jam, 4atj sisyphus luke Seek mukundan, JRKX, jailctf merger, intgrah jimboko awu macaque sammyuri, jonas ryno kg583 kabutack, xsot ovs att joking mewheni, jonas ryno kg583) / others: 59(Yuchen20), 59(jacekwl Potatoman nauti), 60(kabutack), 61(HETHAT), 67(azakhtyamov)
# lambda g:[[*r]for r in zip(*g[:3])]!=g[:3]and g[:3]or p(g[3:])
# lambda g:[*map(list,zip(*g[:3]))]!=g[:3]and g[:3]or p(g[3:])
# lambda g:p(g[3:])if[*map(list,zip(*g[:3]))]==g[:3]else g[:3]
# lambda g:(a:=g[:3])!=[*map(list,zip(*a))]and a or p(g[3:])
# lambda g:a if(a:=g[:3])!=[*map(list,zip(*a))]else p(g[3:])
# ========================== 58 ==========================
p=lambda g:p(g[3:])if(a:=g[:3])==[*map(list,zip(*a))]else a
