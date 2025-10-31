# best: 123(lv1.dev, LogicLynx, FuunAgent) / others: 124(ALE-Agent), 125(Code Golf International), 126(ox jam), 127(jailctf merger), 128(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ========================================================== 123 ==========================================================
import re;p=lambda g,c=-15:c*g or[*zip(*eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(16):
#   g=eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
