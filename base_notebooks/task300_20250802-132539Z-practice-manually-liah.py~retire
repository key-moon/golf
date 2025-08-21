
def p(m):
 a=[(i,j)for i,r in enumerate(m)for j,v in enumerate(r)if v]
 if not a:return[]
 from collections import Counter as C
 v=C(m[i][j]for i,j in a).most_common(1)[0][0]
 x=[(i,j)for i,j in a if m[i][j]==v]
 r0,c0=min(i for i,_ in x),min(j for _,j in x)
 r1,c1=max(i for i,_ in x)+1,max(j for _,j in x)+1
 return[m[i][c0:c1]for i in range(r0,r1)]

