def	p(m):
	F,G=len(m),len(m[0]);A,C={},[r[:]for	r	in	m]
	for	r	in	range(F):
		for	c	in	range(G):
			v=m[r][c]
			if	v:A.setdefault(v,[]).append((r,c))
	for	v	in	A:
		(B,D),(E,H)=A[v];I=1if	E>B	else-1;J=1if	H>D	else-1
		for	i	in	range(abs(E-B)+1):C[B+i*I][D+i*J]=v
	return	C