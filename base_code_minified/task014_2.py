def p(A):
	C={}
	for D in A:
		for B in D:
			if B:C[B]=C.get(B,0)+1
	K=min(C,key=C.get);E,L,M=len(A),len(A),0;F,G=len(A[0]),0
	for(H,D)in enumerate(A):
		for(I,B)in enumerate(D):
			if B==K:E=min(E,H);G=max(G,H);F=min(F,I);J=max(J,I)
	return[A[F:J+1]for A in A[E:G+1]]