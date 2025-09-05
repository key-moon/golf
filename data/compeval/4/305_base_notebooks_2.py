def	p(j):
	A=len(j);c=[x	for	r	in	j	for	x	in	r	if	x]
	if	not	c:return	j
	B=sorted(set(c));k=len(B);C=[[0]*A	for	_	in[0]*A]
	for	l	in	range(A):
		for	D	in	range(A):C[l][D]=B[(l+D)%k]
	return	C