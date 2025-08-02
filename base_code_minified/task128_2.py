def p(A):
	I,J=len(A),len(A[0]);D=[I]*5;E=[-1]*5
	for(C,F)in enumerate(A):
		for(G,B)in enumerate(F):
			if B:
				if C<D[B]:D[B]=C
				if C>E[B]:E[B]=C
	H=[[0]*J for A in A]
	for(C,F)in enumerate(A):
		for(G,B)in enumerate(F):
			if B:H[C-(E[B]-D[B]+1)][G]=B
	return H