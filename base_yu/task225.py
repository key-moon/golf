# best: 132(xsot ovs att joking mewheni) / others: 136(jailctf merger), 145(4atj sisyphus luke Seek mukundan), 145(4atj sisyphus luke Seek), 194(jonas ryno kg583), 204(Yuchen20)
# ============================================================== 132 ===============================================================
import re;p=lambda g,c=-15:c*g or[*zip(*eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(16):
#   g=eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
