# best: 131(jailctf merger) / others: 145(mukundan), 163(4atj sisyphus luke Seek), 189(xsot ovs att joking mewheni), 208(MasukenSamba), 215(kg583)
# ============================================================== 131 ==============================================================
import re
p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("%d, ([^\]0%d])(,.+%d.{34})0"%(d:=max(max(g),key=bool),d,d),r"%d,0\2 \1"%d,str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  c=max(max(g),key=bool)
#  for _ in range(4):
#   g=eval(re.sub("%d, ([^\]0%d])(,.+%d.{34})0"%(c,c,c),r"%d,0\2 \1"%c,str(g)))
#   g=[*zip(*g[::-1])]
#  return g

