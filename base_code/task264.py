def p(g):
 h,w=len(g),len(g[0])
 L=[(i,j,T)for i in range(h-2)for j in range(w-2)
    for T in[tuple(g[i+u][j+v]for u in range(3)for v in range(3))]
    if any(T)]
 D={}
 for _,T in L:D[T]=D.get(T,0)+1
 L=[(i,j,T)for i,j,T in L if D[T]==1]
 L.sort(key=lambda x:(-x[0],-x[1]))
 R=[[0]*9 for _ in range(9)]
 for k,(i,j,T) in enumerate(L):
    y=k//3*3; x=k%3*3
    for p in range(9): R[y+p//3][x+p%3]=T[p]
 return R
