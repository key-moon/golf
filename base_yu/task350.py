# best: 91(4atj sisyphus luke Seek mukundan) / others: 94(jailctf merger), 96(xsot ovs att joking mewheni), 101(kabutack), 107(jonas ryno kg583), 117(natte)
# =========================================== 91 ==========================================
# port re;p=lambda g,c=-47:g*c or eval(re.sub("(1[^(]*)0([^(]*1)",r"\1 8\2",str([*zip(*p(g,c+1))][::-1])))
p=lambda g,c=-1:c*g or p([[v or(1in s[:i])*(1in s[i:])*8for i,v in enumerate(s)]for s in zip(*g)],c+1)













