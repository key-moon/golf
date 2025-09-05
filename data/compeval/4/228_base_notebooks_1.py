j=lambda	A:[[A[B][c]for	B	in	range(len(A))]for	c	in	range(len(A[0]))]
def	J(A):c=[A	for(A,c)in	enumerate(A)if	any(c)];return	c[0],c[-1]
def	p(A):
	c,B=J(A);k,C=J(j(A))
	def	D(l,J,a,C):A[l][J],A[a][C]=A[a][C],A[l][J]
	D(c+1,k+1,B+1,C+1);D(c+1,C-1,B+1,k-1);D(B-1,k+1,c-1,C+1);D(B-1,C-1,c-1,k-1);return	A