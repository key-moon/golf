def p(g):
	F,G=len(g),len(g[0]);O=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];(I,J,K),(H,L,E)=O;M,N=abs(H-I),abs(L-J);D=[[0]*G for A in range(F)]
	if N<=M:
		B=N*2
		for A in range(F):
			for C in range(G):
				if(C-J)%B==0:D[A][C]=K
				if(C-L)%B==0:D[A][C]=E
	else:
		B=M*2
		for A in range(F):
			for C in range(G):
				if(A-I)%B==0:D[A][C]=K
				if(A-H)%B==B-E%B:D[A][C]=E
				if(A-H)%B==0:D[A][C]=E
	return D