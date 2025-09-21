# best: 63(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 107(jacekw Potatoman nauti), 107(jacekwl Potatoman nauti), 110(Yuchen20), 111(natte), 116(MasukenSamba)
# ============================= 63 ============================
# p=lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[(5in g[-1-c%2])-2::-1])],c+1)
p=lambda g,c=47:-c*g or p([*zip(*g[(5in g[~c|62])-2::-1])],c-1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1
