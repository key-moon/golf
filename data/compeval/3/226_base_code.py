def	p(g):
	h=len(g);w=len(g[0]);y=[i	for(i,r)in	enumerate(g)if	r.count(5)==w];x=[j	for	j	in	range(w)if	all(g[i][j]==5for	i	in	range(h))];A=[-1]+y+[h];B=[-1]+x+[w];b=[(A[i]+1,A[i+1]-1)for	i	in	range(len(A)-1)if	A[i]+1<A[i+1]];c=[(B[i]+1,B[i+1]-1)for	i	in	range(len(B)-1)if	B[i]+1<B[i+1]];C=len(b);D=len(c)
	for	k	in	range(3):
		v=k+1;E=(0,(C-1)//2,C-1)[k];F=(0,(D-1)//2,D-1)[k];a,G=b[E];H,I=c[F]
		for	r	in	range(a,G+1):
			for	j	in	range(H,I+1):g[r][j]=v
	return	g