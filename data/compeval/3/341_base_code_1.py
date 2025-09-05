def	p(g):
	A={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v	and	v^8:
				if	v	in	A:a,b,c,e=A[v];A[v]=[min(a,i),max(b,i),min(c,j),max(e,j)]
				else:A[v]=[i,i,j,j]
	(a,b,c,e),(f,h,d,k)=A.values();B=lambda	A,B,C,D:range(max(A,C)+1,min(B,D))or	range(B+1,C)or	range(D+1,A)
	for	i	in	B(a,b,f,h):
		for	j	in	B(c,e,d,k):g[i][j]=8
	return	g