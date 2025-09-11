# best: 111(jailctf merger) / others: 112(4atj sisyphus luke Seek mukundan), 119(xsot ovs att joking mewheni), 129(natte), 136(dbdr), 138(MasukenSamba)
# f p(g):i=sum(g,[]).index(8)//10;*x,=filter(int,sum([*zip(*g[:i]),*zip(*g[i+2:])],()));return[[v==8 and x.pop(0)for v in s]for s in g]
# ==================================================== 111 ====================================================
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("([1-9])((.{32})+?[^[(]+?)8",r"0\2\1",str(p(g,c+1)))))][::-1]
