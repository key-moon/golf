def	p(j):
	B,c=len(j),len(j[0])
	for	A	in	range(B-1):
		for	k	in	range(c-1):
			if	j[A][k]==j[A][k+1]==j[A+1][k]==j[A+1][k+1]==5:
				if	A>0and	k>0:j[A-1][k-1]=1
				if	A>0and	k+2<c:j[A-1][k+2]=2
				if	A+2<B	and	k>0:j[A+2][k-1]=3
				if	A+2<B	and	k+2<c:j[A+2][k+2]=4
	return	j