def p(m):
 E=enumerate
 a=[(i,j)for i,r in E(m)for j,v in E(r)if v]
 if not a:return[]
 from collections import Counter as C
 v=C(m[i][j]for i,j in a).most_common(1)[0][0]
 x=[(i,j)for i,j in a if m[i][j]==v]
 k,g=min(i for i,_ in x),min(j for _,j in x)
 n,X=max(i for i,_ in x)+1,max(j for _,j in x)+1
 return[m[i][g:X]for i in range(k,n)]