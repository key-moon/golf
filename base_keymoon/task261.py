# best: 47(ox jam, 4atj sisyphus luke Seek mukundan, Rafael Pooja, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, HETHAT, xsot ovs att joking mewheni) / others: 48(natte), 48(duckyluuk), 50(JRKX), 50(jacekw Potatoman nauti), 50(kabutack)
# lambda g:[[0]*len(g),*eval(str(g).replace(*"82"))[:-1]]
# lambda g:eval(str(g*2).replace(*"82"))[len(g)-1:-1]
# lambda g:[g[-1],*eval(str(g).replace(*"82"))[:-1]]
# lambda g:[g[-1]]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# ===================== 47 ====================
p=lambda g:[[c/4for c in r]for r in[g.pop()]+g]
