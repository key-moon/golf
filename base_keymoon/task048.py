# 2つの2のブロックが繋がっているか regexで置換しまくる
# g=[re.sub("81|21","11","".join(map(str,r))) for r in zip(*g[::-1])]
# g=[re.sub("81|21|12|18","11","".join(map(str,r))) for r in zip(*g)]

# 8-("2"in str(g))*8
# ("2"not in str(g))*8
# str(g).count("2")

# これ最短99らしいので方針違うんだろうな〜

# 171
# import re
# def p(g):
#  g=eval(str(g).replace("2","1",1))
#  for x in range(99):
#   g=[re.sub("81|21","11","".join(map(str,r))) for r in zip(*g[::-1])]
#  return[[8-("2"in str(g))*8]]

# 167
# d=re.sub(r'\D','',str(g).replace("2","1",1).replace("],","3"))
# d=re.sub('[[ ,]','',str(g)).replace("2","1",1)
# d=re.sub("2","3",re.sub('[[ ,]','',str(g)),1)
# d=re.sub(f"(8|2)(?=(.{{{len(g[0])}}})?1)","1",d)[::-1]
# d=re.sub("(8|2)(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
# [8-("2"in d)*8]
# [0,8]["2"in d]
# from re import* <- 156
# import re;s=re.sub # <- 153
import re;s=re.sub # <- 153
def p(g):
 d=s("2","1",s("[[ ,]","",str(g)),1)
 for x in d:
  d=s("(8|2)(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
 return[[[8,0]["2"in d]]]
