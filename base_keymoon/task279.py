# best: 107(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 111(4atj sisyphus luke Seek mukundan), 112(biz), 113(ox jam), 120(import itertools), 129(THUNDER THUNDER)
# ================================================== 107 ==================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*["9(?=, 9\.|\))","1(?=, 9,|, 8)","9.","8"][c>64::2],str(p(g,c-1)))))][::-1]
