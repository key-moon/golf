# best: 94(jailctf merger) / others: 100(joking), 100(joking MeWhenI), 102(4atj sisyphus luke Seek), 102(sisyphus), 114(Seek64)
# 類題: 081
# port re;p=lambda g,c=-63:c*g or p(eval(re.sub("0(, [47].{25}[47])","7\\1",str([*zip(*g[::-1])]))),c+1)
# ============================================ 94 ============================================
import re;p=lambda g,c=-11:c*g or p(eval(re.sub("0(?=, [47].{25}[47])","7",str([*zip(*g[::-1])]))),c+1)
