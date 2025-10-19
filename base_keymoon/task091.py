# best: 63(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 64(MasukenSamba), 92(THUNDER THUNDER), 107(jacekwl Potatoman nauti), 107(jacekw Potatoman nauti), 110(ShadowPrompt Labs)
# ============================= 63 ============================
# p=lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[(5in g[-1-c%2])-2::-1])],c+1)
p=lambda g,c=47:-c*g or p([*zip(*g[(5in g[~c|62])-2::-1])],c-1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1
