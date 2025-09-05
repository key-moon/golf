j=lambda	A:[[A[B][x]for	B	in	range(len(A))]for	x	in	range(len(A[0]))]
def	p(A):
	c,C=len(A),len(A[0])
	if	C>c:return	j(p(j(A)))
	k,B,l=0,c,0
	for(D,a)in	enumerate(A):
		if	a[0]==2:k=D
		if	any(i==3for	i	in	a):B,l=min(B,D),D
	if	B<k:return	p(A[::-1])[::-1]
	return	A[:k+1]+A[B:l+1]+[[8]*C]+[[0]*C]*(c-k+B-l-3)