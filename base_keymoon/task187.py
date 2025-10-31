# best: 83(jailctf merger) / others: 88(LogicLynx), 88(ox jam), 90(FuunAgent), 91(Code Golf International), 91(lv1.dev)
# ======================================= 83 ======================================
# port re;p=lambda g,c=-63:g*c or[*zip(*eval(re.sub(*['2(?=, 3|\))',*'032'][c>=0::2],str(p(g,c+1)))))][::-1]
# port re;S=re.sub;p=lambda g,c=-63:g*c or eval(S("2(?=, 3|\))","3",S(*"02",str([*zip(*p(g,c+1))][::-1]))))
# port re;S=re.sub;p=lambda g,c=-127:S(*"02",str(g))*c or[*zip(*eval(S("2(?=, 3|\))","3",str(p(g,c+1)))))][::-1]
import re;S=re.sub;p=lambda g,c=-63:g*c or[*zip(*eval(S("2(?=, 3|\))","3",S(*"02",str(p(g,c+1))))))][::-1]

# import re
# S=re.sub
# p=lambda g,c=-63:g*c or[*zip(*eval(S(*['2(?=, 3|\))',*'032'][::2],S(*'02',str(p(g,c+1))))))][::-1]
