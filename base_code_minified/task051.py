def p(A):
	H=sum(A,[]);I=next(A for A in H if H.count(A)<2);B,C=len(A),len(A[0]);E,F=next((A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==I);J=max((0,1),(0,-1),(1,0),(-1,0),key=lambda K:sum(0<=E+K[0]*D<B and 0<=F+K[1]*D<C and A[E+K[0]*D][F+K[1]*D]==0 for D in range(1,B+C)))
	for K in range(1,B+C):
		D,G=E+J[0]*K,F+J[1]*K
		if 0<=D<B and 0<=G<C and A[D][G]==0:A[D][G]=I
	return A