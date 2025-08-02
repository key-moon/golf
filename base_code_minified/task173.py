def p(A):
	K,L=len(A),len(A[0]);N={}
	for(I,J)in((0,1),(1,1)):
		for B in range(K):
			for C in range(L):
				D,E=B-I,C-J;F,G=B+I,C+J
				if 0<=D<K and 0<=E<L and 0<=F<K and 0<=G<L:
					H=A[D][E];M=A[B][C];P=A[F][G]
					if H and H==P and M and M!=H:N[I,J]=H,M;break
			if(I,J)in N:break
	if(0,1)in N:
		H,M=N[0,1];O=[(0,1),(0,-1),(1,0),(-1,0)]
		for B in range(K):
			for C in range(L):
				for(I,J)in O:
					D,E=B-I,C-J;F,G=B+I,C+J
					if 0<=D<K and 0<=E<L and 0<=F<K and 0<=G<L:
						if A[B][C]==M and not A[D][E]and not A[F][G]:A[D][E]=A[F][G]=H
						if not A[B][C]and A[D][E]==H and A[F][G]==H:A[B][C]=M
	if(1,1)in N:
		H,M=N[1,1];O=[(1,1),(1,-1),(-1,1),(-1,-1)]
		for B in range(K):
			for C in range(L):
				for(I,J)in O:
					D,E=B-I,C-J;F,G=B+I,C+J
					if 0<=D<K and 0<=E<L and 0<=F<K and 0<=G<L:
						if A[B][C]==M and not A[D][E]and not A[F][G]:A[D][E]=A[F][G]=H
						if not A[B][C]and A[D][E]==H and A[F][G]==H:A[B][C]=M
	return A