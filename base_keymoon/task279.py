# best: 106(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 107(ox jam), 109(Code Golf International), 111(4atj sisyphus luke Seek mukundan), 112(biz), 114(santa2024)
# ================================================= 106 ==================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*["9(?=, 9\.|\))","1(?=, 9,|, 8)","9.","8"][c>64::2],str(p(g,c-1)))))][::-1]
