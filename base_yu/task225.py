# best: 127(jailctf merger) / others: 129(jacekw Potatoman nauti natte), 129(jacekw Potatoman nauti), 132(ox jam), 138(biz), 142(Yuchen20)
# ============================================================ 127 ============================================================
import re;p=lambda g,c=-15:c*g or[*zip(*eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(p(g,c+1))))[::-1])]


# import re
# def p(g):
#  for _ in range(16):
#   g=eval(re.sub(r"(0.{16}0, ([^0]), (?!\2|0).{43}(...)?(.{20})?)0",r"\1\2",str(g)))
#   g=[*zip(*g[::-1])]
#  return g
