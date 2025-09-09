# best: 51(4atj sisyphus luke Seek mukundan, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 52(jailctf merger), 55(4atj sisyphus luke Seek), 59(HETHAT), 61(natte), 61(mukundan)
# ======================= 51 ======================
# p=lambda g,c=-1:g*c or p([u:=[8]*len(g)]+[*zip(*g)][2:]+[u],c+1)
# p=lambda g:[a:=[8]*len(g[0])]+[[8,*r[2:],8]for r in g[2:]]+[a]
p=lambda g:[a:=[8]*len(g[0]),*[[8,*r[2:],8]for r in g[2:]],a]
# p=lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a
