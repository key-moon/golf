# best: 51(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, ox jam, MasukenSamba, intgrah jimboko awu macaque sammyuri, import itertools) / others: 56(THUNDER THUNDER), 59(HETHAT), 61(cubbus), 62(Yuchen20), 63(biz)
# ======================= 51 ======================
# p=lambda g,c=-1:g*c or p([u:=[8]*len(g)]+[*zip(*g)][2:]+[u],c+1)
# p=lambda g:[a:=[8]*len(g[0])]+[[8,*r[2:],8]for r in g[2:]]+[a]
p=lambda g:[a:=[8]*len(g[0]),*[[8,*r[2:],8]for r in g[2:]],a]
# p=lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a
