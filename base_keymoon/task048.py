# 2つの2のブロックが繋がっているか regexで置換しまくる
# g=[re.sub("81|21","11","".join(map(str,r))) for r in zip(*g[::-1])]
# g=[re.sub("81|21|12|18","11","".join(map(str,r))) for r in zip(*g)]

# 8-("2"in str(g))*8
# ("2"not in str(g))*8
# str(g).count("2")

# これ最短99らしいので方針違うんだろうな〜

import re
def p(g):
 w=len(g[0])
 for x in range(99):
  if g[i:=x//w][j:=x%w]&2:g[i][j]=1;break
 for x in range(99):
  g=[re.sub("81|21","11","".join(map(str,r))) for r in zip(*g[::-1])]
 return[[8-("2"in str(g))*8]]
