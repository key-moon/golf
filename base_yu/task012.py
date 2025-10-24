# best: 126(jailctf merger) / others: 132(jacekw Potatoman nauti natte), 132(import itertools), 132(ox jam), 133(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 133(Code Golf International)
# =========================================================== 126 ============================================================
import re
p=lambda g,c=-7:c*g or[*zip(*eval(re.sub(r"(([^0]), ([^0]), )0(.{31}\3, )0(.{40})0",r"\1\3\4\2\5\2",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(8):
#   g=eval(re.sub(r"(([^0]), ([^0]), \2, )0(.{31}\2, )0(.{40})0",r"\1\2\4\3\5\3",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
