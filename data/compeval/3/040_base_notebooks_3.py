def	p(j):
	B=range;c=[A[:]for	A	in	j];C=j[0][0]==j[0][9];k,D=(j[0][0],j[9][0])if	C	else(j[0][0],j[0][9]);l=next(A	for	a	in	j	for	A	in	a	if	A	and	A	not	in[k,D])
	for	A	in	B(10):
		for	a	in	B(10):
			if	j[A][a]==l:E=(A,9-A)if	C	else(a,9-a);c[A][a]=k	if	E[0]<E[1]else	D
	return	c