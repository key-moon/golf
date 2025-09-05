def	p(g):
	r,c=len(g),len(g[0]);H=[i	for	i	in	range(r)if	g[i][0]and	g[i]==[g[i][0]]*c];I=[j	for	j	in	range(c)if	g[0][j]and	all(g[i][j]==g[0][j]for	i	in	range(r))];E=[-1]+H+[r];F=[-1]+I+[c];G=[(E[a]+1,E[a+1],F[b]+1,F[b+1])for	a	in	range(len(E)-1)for	b	in	range(len(F)-1)]
	for(A,B,C,D)in	G:
		if	any(g[i][j]for	i	in	range(A,B)for	j	in	range(C,D)):J=[A[C:D]for	A	in	g[A:B]];K=A,B,C,D;break
	for(A,B,C,D)in	G:
		if(A,B,C,D)!=K:
			for	i	in	range(A,B):g[i][C:D]=J[i-A]
	return	g