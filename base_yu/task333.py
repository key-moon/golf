# best: 89(jailctf merger, xsot ovs att joking mewheni) / others: 94(4atj sisyphus luke Seek mukundan), 102(jacekwl Potatoman nauti), 104(kabutack), 110(intgrah jimboko awu macaque sammyuri), 142(J&R)
# ========================================== 89 =========================================
# lambda g,c=-3:c*g or p([[v or(3in s[:i])*max(s[i:])for i,v in enumerate(s)]for s in zip(*g[::-1])],c+1)
# lambda g,c=-3:c*g or p([[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or[[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*p(g,c+1)[::-1])]
