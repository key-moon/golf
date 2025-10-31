# best: 84(jailctf merger) / others: 88(Code Golf International), 88(intgrah jimboko awu macaque sammyuri), 89(4atj sisyphus luke Seek mukundan), 89(ox jam), 91(lv1.dev)
# ======================================= 84 =======================================
# copied from 002
import re;p=lambda g,c=63:-c*g or[*zip(*eval(re.sub(*["1(?=, 0|\))",*"001"][c<1::2],str(p(g,c-1)))))][::-1]
