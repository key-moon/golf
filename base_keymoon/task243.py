# best: 79(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 80(intgrah jimboko awu macaque sammyuri), 88(duckyluuk), 90(kabutack), 96(HashPanda), 98(MasukenSamba)
# bestは正規表現じゃないんだろうが、一旦正規表現に甘えます
import re;s=re.sub
def p(g):
 d=s("[[ ,]","",str(g))
 for x in d+d:d=s("0(?=("+"."*len(g)+")?1)","1",d)[::-1]
 return [[*map(int,r)]for r in d.split("]")[:-2]]

