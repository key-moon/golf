# best: 73(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, FuunAgent, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, biz, intgrah jimboko awu macaque sammyuri) / others: 74(jonas ryno kg583 kabutack), 74(jacekwl Potatoman nauti), 74(JRK), 74(JRKX), 74(jacekwl)
# ================================== 73 =================================
p=lambda g:[[[5,v][v==max(a:=sum(g,g),key=a.count)]for v in s]for s in g]

# p=lambda g:[[[5,v][v==__import__("collections").Counter(sum(g,[])).most_common()[0][0]]for v in s]for s in g]
