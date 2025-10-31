# best: 105(jailctf merger) / others: 106(ox jam), 110(Code Golf International), 110(biz), 112(4atj sisyphus luke Seek mukundan), 112(lv1.dev)
# ================================================= 105 =================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*[" 0(?=, 0\.|\))","1(?=, 0,|, 3)","0.","3"][c>64::2],str(p(g,c-1)))))][::-1]
