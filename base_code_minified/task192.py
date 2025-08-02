def p(A):
	K=sum(A,[]);L=set(K)-{0};C=min(L,key=K.count);M=(L-{C}).pop();E,F=len(A),len(A[0]);D=[(B,D)for B in range(E)for D in range(F)if A[B][D]==C and(B<1 or B>E-2 or D<1 or D>F-2)]
	while D:
		G,B=D.pop()
		if A[G][B]==C:
			A[G][B]=0
			for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
				H,I=G+N,B+O
				if 0<=H<E and 0<=I<F and A[H][I]==C:D.append((H,I))
	for J in A:
		for B in range(len(J)):
			if J[B]==C:J[B]=M
	return A