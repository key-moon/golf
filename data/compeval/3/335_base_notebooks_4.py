def p(g,R=range):
	F=lambda v:next((B,A.index(v))for(B,A)in enumerate(g)if v in A);C,A=F(8);B,D=F(2)
	for E in R(C+1,B+1)if C<B else R(B,C):g[E][A]=4
	for E in R(A,D)if A<D else R(D+1,A):g[B][E]=4
	return g
