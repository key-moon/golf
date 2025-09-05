# best: 63(xsot ovs att joking mewheni, jailctf merger) / others: 92(4atj sisyphus luke Seek), 96(mukundan), 111(natte), 122(MasukenSamba), 127(kabutack)
# ============================= 63 ============================
# lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1