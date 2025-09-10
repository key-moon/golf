# best: 127(jailctf merger) / others: 133(xsot ovs att joking mewheni), 133(4atj sisyphus luke Seek mukundan), 133(4atj sisyphus luke Seek), 138(biz), 147(mukundan)
# ============================================================ 127 ============================================================
import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub(r"(([^0]), ([^0]), )0(.{31}\3, )0(.{40})0",r"\1\3\4\2\5\2",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(8):
#   g=eval(re.sub(r"(([^0]), ([^0]), \2, )0(.{31}\2, )0(.{40})0",r"\1\2\4\3\5\3",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
