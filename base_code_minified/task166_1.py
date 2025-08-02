def p(A):
	E,F=len(A),len(A[0]);B=[A[:]for A in A]
	for C in range(E):
		for D in range(F):
			if B[C][D]==0:B[C][D]=2
	G=[(0,A)for A in range(F)]+[(E-1,A)for A in range(F)]+[(A,0)for A in range(E)]+[(A,F-1)for A in range(E)]
	while G:
		C,D=G.pop()
		if B[C][D]==2:
			B[C][D]=0
			for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
				H,I=C+J,D+K
				if 0<=H<E and 0<=I<F and B[H][I]==2:G.append((H,I))
	return B