# best: 105(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 156(jacekwl Potatoman nauti), 167(intgrah jimboko awu macaque sammyuri), 170(natte), 177(Afordancja), 187(Yuchen20)
# ================================================= 105 =================================================
# lambda g,c=-1,a=0:g*c or p([*zip(*[[(v or(c+3in s)*8)*(a|(a:=a^any(t)))for*t,v in zip(*g,s)]for s in g])],c+1)
p=lambda g,c=1,a=0:g*-c or p([[(v or(c+2in s)*8)*(a|(a:=a^any(t)))for t,v in zip(g,s)]for s in zip(*g)],c-1)
