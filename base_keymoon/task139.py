# best: 94(jailctf merger) / others: 99(4atj sisyphus luke Seek mukundan), 100(xsot ovs att joking mewheni), 114(kabutack), 134(jacekwl Potatoman nauti), 138(natte)
# 類題: 081
# port re;p=lambda g,c=-63:c*g or p(eval(re.sub("0(, [47].{25}[47])","7\\1",str([*zip(*g[::-1])]))),c+1)
# ============================================ 94 ============================================
import re;p=lambda g,c=-11:c*g or[*zip(*eval(re.sub("0(?=, [47].{25}[47])","7",str(p(g,c+1)))))][::-1]





