# best: 111(jailctf merger) / others: 112(4atj sisyphus luke Seek mukundan), 112(ox jam), 115(intgrah jimboko awu macaque sammyuri), 135(import itertools), 138(jacekw Potatoman nauti natte)
# ==================================================== 111 ====================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*[" 0(?=, 0\.|\))","1(?=, 0,|, 3)","0.","3"][c>64::2],str(p(g,c-1)))))][::-1]
