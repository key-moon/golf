# best: 90(jailctf merger) / others: 92(4atj sisyphus luke Seek mukundan), 95(ox jam), 96(jacekw Potatoman nauti natte), 96(jacekw Potatoman nauti), 102(jacekwl Potatoman nauti)
# 類題: 139
# ========================================== 90 ==========================================
# p=lambda g,c=-3:c*g or p([s for s in zip(*g[::-1])],c+1)
# import re;p=lambda g,c=-7:c*g or p(eval(re.sub("(8.{19}8, )0","\\1 1",str([*zip(*g[::-1])]))),c+1)
import re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(g,c+1)))))][::-1]
