# best: 106(jailctf merger) / others: 107(Code Golf International), 108(ox jam), 111(HIMAGINE THE FUTURE.), 112(4atj sisyphus luke Seek mukundan), 117(import itertools)
# f p(g):i=sum(g,[]).index(8)//10;*x,=filter(int,sum([*zip(*g[:i]),*zip(*g[i+2:])],()));return[[v==8 and x.pop(0)for v in s]for s in g]
# ================================================= 106 ==================================================
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("([1-9])((.{32})+?[0, ]+)8",r"0\2\1",str(p(g,c+1)))))][::-1]
