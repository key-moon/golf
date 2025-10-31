# best: 81(biz) / others: 86(santa2024), 88(ox jam), 89(jailctf merger), 92(Code Golf International), 95(intgrah jimboko awu macaque sammyuri)
# 類題: 081
# port re;p=lambda g,c=-63:c*g or p(eval(re.sub("0(, [47].{25}[47])","7\\1",str([*zip(*g[::-1])]))),c+1)
# ====================================== 81 =====================================
import re;p=lambda g,c=-11:c*g or[*zip(*eval(re.sub("0(?=, [47].{25}[47])","7",str(p(g,c+1)))))][::-1]
