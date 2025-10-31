# best: 116(Code Golf International, jailctf merger, ox jam) / others: 119(jacekw Potatoman nauti natte), 119(import itertools), 120(natte), 121(LogicLynx), 122(biz)
# ====================================================== 116 =======================================================
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("%d, ([^\]0%d])(,.+%d.{34})0"%(d:=max(max(g),key=bool),d,d),r"%d,0\2 \1"%d,str(p(g,c+1))))[::-1])]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"(?<=([1-9]), )((?!\1)[1-9])((.{32}){2,}, \1(, \1)+.{34})0",r"0\3\2",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"(?<=([^0]), )((?!\1).)((.{32})+(, \1)+.{34})0",r"0\3\2",str(p(g,c+1)))))][::-1]
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"(?<=([^0], ))((?!\1).)(, (.{32})+\1+.{32})0",r"0\3\2",str(p(g,c+1)))))][::-1]


# import re
# def p(g):
#  c=max(max(g),key=bool)
#  for _ in range(4):
#   g=eval(re.sub("%d, ([^\]0%d])(,.+%d.{34})0"%(c,c,c),r"%d,0\2 \1"%c,str(g)))
#   g=[*zip(*g[::-1])]
#  return g
