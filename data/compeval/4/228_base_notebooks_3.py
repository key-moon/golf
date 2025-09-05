j=lambda	A:[[A[C][B]for	C	in	range(len(A))]for	B	in	range(len(A[0]))]
def	l(A):c=[i	for(i,r)in	enumerate(A)if	any(r)];return	c[0],c[-1]
def	p(A):
	B,k=l(A);C,p=l(j(A))
	def	s(c,l,J,a):A[c][l],A[J][a]=A[J][a],A[c][l]
	s(B+1,C+1,k+1,p+1);s(B+1,p-1,k+1,C-1);s(k-1,C+1,B-1,p+1);s(k-1,p-1,B-1,C-1);return	A