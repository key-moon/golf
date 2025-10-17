# best: 73(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, ox jam, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 74(kabutack), 74(jonas ryno kg583), 74(JRKKX), 74(jacekwl), 74(THUNDER THUNDER)
# ================================== 73 =================================
p=lambda g:[[[5,v][v==max(a:=sum(g,g),key=a.count)]for v in s]for s in g]

# p=lambda g:[[[5,v][v==__import__("collections").Counter(sum(g,[])).most_common()[0][0]]for v in s]for s in g]
