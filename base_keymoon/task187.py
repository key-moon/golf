# best: 94(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 97(jacekwl Potatoman), 97(jacekwl), 104(4atj sisyphus luke Seek), 106(xsot ovs att joking mewheni), 106(mukundan)
# ============================================ 94 ============================================
# port re;p=lambda g,c=-63:g*c or[*zip(*eval(re.sub(*['2(?=, 3|\))',*'032'][c>=0::2],str(p(g,c+1)))))][::-1]
# port re;S=re.sub;p=lambda g,c=-63:g*c or eval(S("2(?=, 3|\))","3",S(*"02",str([*zip(*p(g,c+1))][::-1]))))
# port re;S=re.sub;p=lambda g,c=-127:S(*"02",str(g))*c or[*zip(*eval(S("2(?=, 3|\))","3",str(p(g,c+1)))))][::-1]
import re;S=re.sub;p=lambda g,c=-63:g*c or[*zip(*eval(S("2(?=, 3|\))","3",S(*"02",str(p(g,c+1))))))][::-1]

# import re
# S=re.sub
# p=lambda g,c=-63:g*c or[*zip(*eval(S(*['2(?=, 3|\))',*'032'][::2],S(*'02',str(p(g,c+1))))))][::-1]
