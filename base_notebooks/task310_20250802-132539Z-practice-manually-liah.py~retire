
from collections import Counter
def p(m):
 c=Counter(e for r in m for e in r if e).most_common()
 if not c: return []
 l=c[-1][0];rs=re=-1
 for i,r in enumerate(m):
  if l in r:
   if rs<0:rs=i
   re=i
 cs=ce=-1
 for i in range(len(m[0])):
  if any(m[j][i]==l for j in range(rs,re+1)):
   if cs<0:cs=i
   ce=i
 return[r[cs:ce+1]for r in m[rs:re+1]]
