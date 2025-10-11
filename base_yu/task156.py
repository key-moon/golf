# best: 146(jailctf merger) / others: 152(4atj sisyphus luke Seek mukundan), 156(ox jam), 186(jacekw Potatoman nauti natte), 186(import itertools), 194(Yuchen20)
# ===================================================================== 146 ======================================================================
# port re;p=lambda g,c=-99:c*g or p([*zip(*eval(re.sub(*["([^0]), 4, 4","(?<=4.{34})4(?=.{34}4(, 4|.{31}4){%d})"%(-c//9),r"\1,\1,4",str(2-("2"in str(g)))][c%9<1::2],str(g))))],c+1)
import re;p=lambda g,c=-99:c*g or p([*zip(*eval(re.sub(*["([^0]), 4, 4","(?<=4.{34})4(?=.{34}4(, 4|.{31}4){%d})"%(-c//9),r"\1,\1,4","21"["2"in str(g)]][c%9<1::2],str(g))))],c+1)

# import re
# def p(g,c=-99):
#  if c>0:
#   return g
#  if c%10<1:
#   g=[*zip(*eval(re.sub("(?<=4.{34})4(?=.{34}4(, 4|.{31}4){%d})"%(-c//10),str(2-("2"in str(g))),str(g))))]
#   return p(g,c+1)
#  else:
#   g=[*zip(*eval(re.sub("([1-9]), 4, 4",r"\1,\1,4",str(g))))]
#   return p(g,c+1)

# import re
# def p(g):
#  for c in range(10)[::-1]:
#   g=eval(re.sub("(?<=4.{34})4(?=.{34}4(, 4|.{31}4){%d})"%c,str(2-("2"in str(g))),str(g)))
#   for _ in range(10):
#    g=[*zip(*eval(re.sub("([1-9]), 4, 4",r"\1,\1,4",str(g))))]
#  return g

# import re
# def p(g):
#  for c in range(2,10)[::-1]:
#   for d in range(1,c):
#    g=eval(re.sub("(?<=4.{34})4(?=(, 4){%d}(.{31}4){%d})"%(d,c-d),str(10-len({*str(g)})),str(g)))
#    for _ in range(10):
#     g=[*zip(*eval(re.sub("([1-9]), 4, 4",r"\1,\1,4",str(g))))]
#  return g
