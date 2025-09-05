def	p(j):
	A=len(j);c=[A	for	c	in	j	for	A	in	c	if	A]
	if	not	c:return	j
	B=sorted(set(c));k=len(B);C=[[0]*A	for	c	in[0]*A]
	for	l	in	range(A):
		for	D	in	range(A):C[l][D]=B[(l+D)%k]
	return	C