def p(A):
	H,I=len(A),len(A[0]);J=[(B,C)for B in range(H)for C in range(I)if A[B][C]]
	while J:
		B,C=J[0];K=[(B,C)];N=[]
		while K:
			B,C=K.pop()
			if(B,C)in J:J.remove((B,C));N.append((B,C));K+=[(B-1,C),(B+1,C),(B,C-1),(B,C+1)]
		O,P=zip(*N);F,L=min(O),max(O);G,M=min(P),max(P);Q=A[F][G];R=A[F+1][G+1]
		for D in range(F-1,L+2):
			for E in range(G-1,M+2):
				if 0<=D<H and 0<=E<I:A[D][E]=R
		for D in(F-1,L+1):
			for E in range(G-1,M+2):
				if 0<=D<H and 0<=E<I:A[D][E]=Q
		for D in range(F-1,L+2):
			for E in(G-1,M+1):
				if 0<=D<H and 0<=E<I:A[D][E]=Q
	return A