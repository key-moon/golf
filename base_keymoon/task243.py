# best: 79(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, biz, intgrah jimboko awu macaque sammyuri) / others: 80(jacekwl Potatoman nauti), 80(jacekw Potatoman nauti natte), 80(jacekw Potatoman nauti), 80(cg-klogw-sekken), 80(natte)
# bestは正規表現じゃないんだろうが、一旦正規表現に甘えます
import re;s=re.sub
def p(g):
 d=s("[[ ,]","",str(g))
 for x in d+d:d=s("0(?=("+"."*len(g)+")?1)","1",d)[::-1]
 return [[*map(int,r)]for r in d.split("]")[:-2]]
