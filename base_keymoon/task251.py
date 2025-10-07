# best: 88(jailctf merger) / others: 89(4atj sisyphus luke Seek mukundan), 89(intgrah jimboko awu macaque sammyuri), 94(HETHAT), 94(ox jam), 97(jacekw Potatoman nauti natte)
# ========================================= 88 =========================================
# copied from 002
import re;p=lambda g,c=63:-c*g or[*zip(*eval(re.sub(*["1(?=, 0|\))",*"001"][c<1::2],str(p(g,c-1)))))][::-1]
