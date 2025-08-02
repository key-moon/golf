def p(A):
	H={}
	for(D,Q)in enumerate(A):
		for(E,I)in enumerate(Q):
			if I:H.setdefault(I,[]).append((D,E))
	(J,B),(K,L)=H.items()
	if B[0][0]==B[1][0]:M=J;F=B[0][0];N=K;G=L[0][1]
	else:M=K;F=L[0][0];N=J;G=B[0][1]
	O,P=len(A),len(A[0]);C=[[0]*P for A in range(O)]
	for D in range(O):C[D][G]=N
	for E in range(P):C[F][E]=M
	C[F][G]=4;return C