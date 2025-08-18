def p(g):
 m,n=len(g),len(g[0])
 R=[i for i,r in enumerate(g)if r[0]and set(r)=={r[0]}]
 C=[j for j in range(n)if g[0][j]and{g[i][j]for i in range(m)}=={g[0][j]}]
 r=[-1]+R+[m];c=[-1]+C+[n]
 return[[g[r[i]+1][c[j]+1]for j in range(len(c)-1)][::-1]for i in range(len(r)-1)]
