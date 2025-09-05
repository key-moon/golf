def	p(j):
	A=[k[:]for	k	in	j];c,C=len(j),len(j[0])
	for	k	in	range(C):
		if	j[0][k]:
			for	B	in	range(c):
				if	B%2==0:A[B][k]=j[0][k]
				else:
					if	k>0:A[B][k-1]=j[0][k]
					if	k<C-1:A[B][k+1]=j[0][k]
	return	A