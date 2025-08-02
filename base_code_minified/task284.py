def p(g):
	N=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];(A,G,K),(I,L,M)=N
	if A==I:
		B=(G+L)//2;O=range(A-2,A+3);J=abs(L-G)//2
		for(P,C)in enumerate(O):
			D=abs(J-1-P);E=B-D;F=B+D+1
			if 0<=C<len(g):
				if 0<=E<len(g[C]):g[C][E]=K
				if 0<=F<len(g[C]):g[C][F]=M
	else:
		B=(A+I)//2;Q=range(G-2,G+3);J=abs(I-A)//2
		for(R,H)in enumerate(Q):
			D=abs(J-1-R);E=B-D;F=B+D+1
			if 0<=E<len(g)and 0<=H<len(g[0]):g[E][H]=K
			if 0<=F<len(g)and 0<=H<len(g[0]):g[F][H]=M
	return g