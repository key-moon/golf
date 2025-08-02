def p(A):
	O=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];(B,H,L),(J,M,N)=O
	if B==J:
		C=(H+M)//2;P=range(B-2,B+3);K=abs(M-H)//2
		for(Q,D)in enumerate(P):
			E=abs(K-1-Q);F=C-E;G=C+E+1
			if 0<=D<len(A):
				if 0<=F<len(A[D]):A[D][F]=L
				if 0<=G<len(A[D]):A[D][G]=N
	else:
		C=(B+J)//2;R=range(H-2,H+3);K=abs(J-B)//2
		for(S,I)in enumerate(R):
			E=abs(K-1-S);F=C-E;G=C+E+1
			if 0<=F<len(A)and 0<=I<len(A[0]):A[F][I]=L
			if 0<=G<len(A)and 0<=I<len(A[0]):A[G][I]=N
	return A