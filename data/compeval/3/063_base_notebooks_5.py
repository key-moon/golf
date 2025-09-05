def	p(j):
	B=range;c=len(j);C=[o[:]for	o	in	j]
	for	k	in	range(c):
		if	j[1][k]==0and	j[c-2][k]==0and	sum(j[A][k]for	A	in	B(1,c-1))==0:
			for	A	in	B(1,c-1):C[A][k]=3
	for	A	in	range(c):
		if	j[A][1]==0and	j[A][c-2]==0and	sum(j[A][k]for	k	in	B(1,c-1))==0:
			for	k	in	B(1,c-1):
				if	C[A][k]==0:C[A][k]=3
	return	C