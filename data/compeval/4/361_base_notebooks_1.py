j=range
A=enumerate
def	W(p,c,E,k):
	for	A	in	j(c,c+k):
		for	l	in	j(E,E+k):
			if	A<len(p)and	l<len(p[0]):
				if	p[A][l]==0:return	0
	return	1
def	l(p):
	C,a=len(p),len(p[0])
	for	l	in	j(a-2,1,-1):
		for	A	in	j(0,C-l):
			for	B	in	j(0,a-l):
				if	W(p,A,B,l):return	A,B,l
	return-1
def	N(p):
	A=0
	for	l	in	p:
		for	a	in	l:
			if	a:A+=1
	return	A
def	b(p,e,K,w,k):
	A=0
	for	l	in	j(e-k,e+w+k):
		for	a	in	j(K-k,K+w+k):
			if	p[l][a]:A+=1
	return	A
def	a(p):
	a,B,C=l(p);D=N(p);A=1
	while	1:
		if	D==b(p,a,B,C,A):return	C+2*A,a-A,B-A
		A+=1
def	C(L):
	b,C=len(L),len(L[0]);B=[A[:]for	A	in	L]
	for(l,D)in	A(L):
		for(a,d)in	A(D):
			if	B[a][C-1-l]==0:B[a][C-1-l]=L[l][a]
	return	B
def	p(L):
	A,l,B=a(L);d=[[0]*A	for	l	in	j(A)]
	for	D	in	j(l,l+A):
		for	b	in	j(B,B+A):d[D-l][b-B]=L[D][b]
	d=C(C(C(d)));f=[A[:]for	A	in	L]
	for	D	in	j(l,l+A):
		for	b	in	j(B,B+A):f[D][b]=d[D-l][b-B]
	return	f