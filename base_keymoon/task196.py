# best: 110(jailctf merger, biz) / others: 112(Code Golf International), 112(4atj sisyphus luke Seek mukundan), 112(ox jam), 123(import itertools), 129(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# =================================================== 110 ====================================================
import re;p=lambda g,c=79:-c*g or[*zip(*eval(re.sub(*[" 0(?=, 0\.|\))","1(?=, 0,|, 3)","0.","3"][c>64::2],str(p(g,c-1)))))][::-1]
