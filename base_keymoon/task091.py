# best: 63(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam) / others: 64(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 64(MasukenSamba), 92(THUNDER THUNDER), 107(jacekwl Potatoman nauti), 107(jacekw Potatoman nauti)
# ============================= 63 ============================
# p=lambda g,c=-47:c*g or p([*zip(*g[1-(5in g[c&1]):][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[5not in g[c&1]:][::-1])],c+1)
# p=lambda g,c=-47:c*g or p([*zip(*g[(5in g[-1-c%2])-2::-1])],c+1)
p=lambda g,c=47:-c*g or p([*zip(*g[(5in g[~c|62])-2::-1])],c-1)

# 1-(5in g[c&1])
# 5not in g[c&1]
# sum({*g[c&1]})&1
