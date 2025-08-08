def p(m):
 from collections import Counter as A;a=[v for r in m for v in r if v];b=dict(A(a).most_common());w=len(m[0]);r=[[0]*w for _ in range(len(m))]
 for(i,k)in enumerate(sorted(b,key=b.get,reverse=True)):r[-1-i][-b[k]:]=[k]*b[k]
 return r