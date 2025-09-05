def	p(j):
	B,c=len(j),len(j[0]);C=lambda	k:next((A,l)for	A	in	range(B-1)for	l	in	range(c-1)if	j[A][l]==j[A+1][l+1]==k);A,l=C(1)
	while	A>=1and	l>=1:A,l=A-1,l-1;j[A][l]=1
	A,l=C(2)
	while	A<B-1and	l<c-1:A,l=A+1,l+1;j[A][l]=2
	return	j