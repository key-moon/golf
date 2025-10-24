# best: 106(intgrah jimboko awu macaque sammyuri) / others: 107(jailctf merger), 111(Code Golf International), 111(4atj sisyphus luke Seek mukundan), 112(biz), 113(ox jam)
# ================================================= 106 ==================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*["9(?=, 9\.|\))","1(?=, 9,|, 8)","9.","8"][c>64::2],str(p(g,c-1)))))][::-1]
