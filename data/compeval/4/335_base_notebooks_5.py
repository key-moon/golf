def	p(j,A=range):
	c=lambda	E:next((l,A.index(E))for(l,A)in	enumerate(j)if	E	in	A);k,B=c(8);l,C=c(2)
	for	a	in	A(k+1,l+1)if	k<l	else	A(l,k):j[a][B]=4
	for	a	in	A(B,C)if	B<C	else	A(C+1,B):j[l][a]=4
	return	j