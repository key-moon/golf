# best: 101(jailctf merger) / others: 104(4atj sisyphus luke Seek), 104(sisyphus), 106(mukundan), 107(joking), 107(joking MeWhenI)
# =============================================== 101 ===============================================
# port re;S=re.sub;p=lambda g,c=-63:g*c or eval(S("2(?=, 3|\))","3",S(*"02",str([*zip(*p(g,c+1))][::-1]))))
import re;S=re.sub;p=lambda g,c=-63:g*c or eval(S("2(?=, 3|\))","3",S(*"02",str([*zip(*p(g,c+1))][::-1]))))
