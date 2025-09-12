# best: 63(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 107(jacekwl Potatoman nauti), 110(Yuchen20), 111(natte), 116(MasukenSamba), 116(intgrah jimboko awu macaque sammyuri)
# ============================= 63 ============================
# lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1
