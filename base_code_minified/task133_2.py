def p(g):
	H=[A[:]for A in g];A={}
	for(E,R)in enumerate(g):
		for(F,I)in enumerate(R):A[I]=A.get(I,[])+[(E,F)]
	S,T,G=[B for B in A if len(A[B])in(1,4)][0],[B for B in A if len(A[B])==4 and B!=[B for B in A if len(A)==1][0]][0],[B for B in A if len(A[B])>4][0];U,J=A[S][0];C=next((0,A-J)for(B,A)in A[T]if B==U and A!=J);C=0,C;K=-C[1],C[0];L=[A for(A,B)in A[G]];M=[A for(B,A)in A[G]];N,O=min(L),max(L);P,Q=min(M),max(M);D=O-N+1;V=Q-P+1
	for B in list(range(V))+[-D,D]:
		if B and abs(B)!=D:continue
		W,X=C[0]*B+K[0]*(B//abs(B)if abs(B)==D else 0),C[1]*B+K[1]*(B//abs(B)if abs(B)==D else 0)
		for E in range(N,O+1):
			for F in range(P,Q+1):
				if g[E][F]==G:H[E+W][F+X]=G
	return H