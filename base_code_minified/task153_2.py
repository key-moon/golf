def p(A):
	B={};[B.setdefault(A,[]).append((C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A];D=[[0]*3 for A in range(3)]
	for E in sorted(B,key=lambda I:min(B[I])):C=B[E];F=next(A for A in C if sum(abs(A[0]-B[0])+abs(A[1]-B[1])==1 for B in C)==2)
	for(G,H)in C:D[G-F[0]+1][H-F[1]+1]=E
	return D