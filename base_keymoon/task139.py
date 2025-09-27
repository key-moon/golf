# best: 90(biz) / others: 93(jailctf merger), 95(intgrah jimboko awu macaque sammyuri), 99(4atj sisyphus luke Seek mukundan), 100(ox jam), 101(JRKX)
# 類題: 081
# port re;p=lambda g,c=-63:c*g or p(eval(re.sub("0(, [47].{25}[47])","7\\1",str([*zip(*g[::-1])]))),c+1)
# ========================================== 90 ==========================================
import re;p=lambda g,c=-11:c*g or[*zip(*eval(re.sub("0(?=, [47].{25}[47])","7",str(p(g,c+1)))))][::-1]
