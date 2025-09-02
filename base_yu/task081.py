# best: 96(4atj sisyphus luke Seek, xsot ovs, luke/sisyphus/Seek, xsot, sisyphus) / others: 105(mukundan), 113(joking+MWI), 113(joking/MWI), 113(kg583), 113(joking MeWhenI)
# 類題: 139
# ============================================= 96 =============================================
# p=lambda g,c=-3:c*g or p([s for s in zip(*g[::-1])],c+1)
# import re;p=lambda g,c=-7:c*g or p(eval(re.sub("(8.{19}8, )0","\\1 1",str([*zip(*g[::-1])]))),c+1)
import re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("0(?=, 8.{19}8)","1",str(p(g,c+1)))))][::-1]
