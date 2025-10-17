# best: 47(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, HETHAT, ox jam, intgrah jimboko awu macaque sammyuri, Rafael Pooja, import itertools) / others: 48(duckyluuk), 48(biz), 50(kabutack), 50(JRKKX), 50(blob2822)
# lambda g:[[0]*len(g),*eval(str(g).replace(*"82"))[:-1]]
# lambda g:eval(str(g*2).replace(*"82"))[len(g)-1:-1]
# lambda g:[g[-1],*eval(str(g).replace(*"82"))[:-1]]
# lambda g:[g[-1]]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# ===================== 47 ====================
p=lambda g:[[c/4for c in r]for r in[g.pop()]+g]
