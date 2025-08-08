A=range
p=lambda g:(n:=len(g))and[[sum(-1<(y:=i+abs(k-2)-1)<n and-1<(x:=j+abs(k-1)-1)<n and g[y][x]>0for k in A(4))>1and g[i][j]for j in A(n)]for i in A(n)]