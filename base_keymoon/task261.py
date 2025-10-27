# best: 47(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, HETHAT, natte, Rafael Pooja, import itertools, jailctf merger, HIMAGINE THE FUTURE., Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 48(biz), 48(duckyluuk), 50(cubbus), 50(jacekwl Potatoman nauti), 50(blob2822)
# lambda g:[[0]*len(g),*eval(str(g).replace(*"82"))[:-1]]
# lambda g:eval(str(g*2).replace(*"82"))[len(g)-1:-1]
# lambda g:[g[-1],*eval(str(g).replace(*"82"))[:-1]]
# lambda g:[g[-1]]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# lambda g:g[-1:]+eval(str(g).replace(*"82"))[:-1]
# ===================== 47 ====================
p=lambda g:[[c/4for c in r]for r in[g.pop()]+g]
