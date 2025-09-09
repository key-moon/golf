# best: 51(4atj sisyphus luke Seek mukundan, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 52(jailctf merger), 59(HETHAT), 61(natte), 65(jonas ryno kg583), 65(JRK)
# lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(g[0])-2),8]]*(len(g)-2)+a
# lambda g,c=-1:g*c or p([*zip(*(a:=[[8]*len(g[0])])+g[1:-1]+a)],c+1)
# lambda g:(a:=[[8]*len(g[0])])+[[8,*[0]*(len(a)-2),8]]*(len(g)-2)+a
# lambda g,c=-1:g*c or p([*zip(*[a:=[8]*len(g[0]),*g[2:],a])],c+1)
# lambda g,c=-3:g*c or p([*zip(*[[8]*len(g[0])]+g[1:])][::-1],c+1)
# lambda g,c=-3:g*c or p([r+[8]for*r,_ in zip(*g[::-1])],c+1)
# lambda g,c=-1:g*c or p([[8,*r,8]for _,*r,_ in zip(*g)],c+1)
# lambda g,c=-1:g*c or p([[8,*r[2:],8]for r in zip(*g)],c+1)
# lambda g,c=-1:g*c or p([[8,*r,8]for*r,_,_ in zip(*g)],c+1)
# ======================= 51 ======================
p=lambda g,c=-1:g*c or[[8,*r[2:],8]for r in zip(*p(g,c+1))]

