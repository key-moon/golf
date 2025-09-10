# best: 51(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 59(HETHAT), 61(natte), 65(jonas ryno kg583), 65(JRK), 66(duckyluuk)
# ======================= 51 ======================
# p=lambda g,c=-1:g*c or p([u:=[8]*len(g)]+[*zip(*g)][2:]+[u],c+1)
# p=lambda g:[a:=[8]*len(g[0])]+[[8,*r[2:],8]for r in g[2:]]+[a]
p=lambda g:[a:=[8]*len(g[0]),*[[8,*r[2:],8]for r in g[2:]],a]
# p=lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a








