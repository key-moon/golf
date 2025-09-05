def	p(g):
	for	F	in	set(sum(g,[])):
		A=[(i,j)for(i,r)in	enumerate(g)for(j,v)in	enumerate(r)if	v==F];B,C=min(A);D,E=max(A)
		if	D-B>1<E-C	and	all(i	in(B,D)or	j	in(C,E)for(i,j)in	A):return[r[C+1:E]for	r	in	g[B+1:D]]