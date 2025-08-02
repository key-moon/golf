def p(A):
	E=len(A);H=[]
	for I in range(E):
		for J in range(E):
			if A[I][J]==8:
				B=[(I,J)];A[I][J]=0
				for(C,D)in B:
					for(F,G)in((C+1,D),(C-1,D),(C,D+1),(C,D-1)):
						if 0<=F<E and 0<=G<E and A[F][G]==8:A[F][G]=0;B.append((F,G))
				H.append(B)
	K=min(map(len,H))
	for B in H:
		for(C,D)in B:A[C][D]=1+(len(B)==K)
	return A