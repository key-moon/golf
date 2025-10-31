# best: 62(Code Golf International, jailctf merger, ox jam) / others: 63(jacekw Potatoman nauti natte), 63(4atj sisyphus luke Seek mukundan), 63(lv1.dev), 63(natte), 63(import itertools)
# ============================ 62 ============================
# p=lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[(5in g[-1-c%2])-2::-1])],c+1)
p=lambda g,c=47:-c*g or p([*zip(*g[(5in g[~c|62])-2::-1])],c-1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1
