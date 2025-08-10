def p(j):
 from collections import Counter as C
 A=[v for k in j for v in k if v]
 c=dict(C(A).most_common())
 E=len(j[0])
 k=[[0]*E for _ in range(len(j))]
 for W,l in enumerate(sorted(c,key=c.get,reverse=True)):k[-1-W][-c[l]:]=[l]*c[l]
 return k