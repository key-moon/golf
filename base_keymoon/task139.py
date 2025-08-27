# best: 100(joking+MWI, joking/MWI, joking, joking MeWhenI) / others: 102(luke/sisyphus/Seek), 102(4atj sisyphus luke Seek), 102(sisyphus), 114(Seek64), 116(mukundan)
# 類題: 081
# ============================================== 100 ===============================================
import re;p=lambda g,c=-63:c*g or p(eval(re.sub("0(, [47].{25}[47])","7\\1",str([*zip(*g[::-1])]))),c+1)

