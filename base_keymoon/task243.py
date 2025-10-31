# best: 75(Code Golf International, lv1.dev, jailctf merger, ox jam) / others: 79(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 79(4atj sisyphus luke Seek mukundan), 79(HIMAGINE THE FUTURE.), 79(biz), 79(intgrah jimboko awu macaque sammyuri)
# bestは正規表現じゃないんだろうが、一旦正規表現に甘えます
import re;s=re.sub
def p(g):
 d=s("[[ ,]","",str(g))
 for x in d+d:d=s("0(?=("+"."*len(g)+")?1)","1",d)[::-1]
 return [[*map(int,r)]for r in d.split("]")[:-2]]
