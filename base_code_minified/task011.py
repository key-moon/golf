def p(A):
	D=len(A);C=[A for(A,B)in enumerate(A)if all(A==5 for A in B)];I=[B for B in range(D)if all(A[C][B]==5 for C in range(D))];C=[-1]+C+[D];I=[-1]+I+[D];E=C[1]-C[0]-1;J=[A[:]for A in A]
	for M in range(3):
		for N in range(3):
			F=C[M]+1;G=I[N]+1;O=[A[B][C]for B in range(F,F+E)for C in range(G,G+E)];B={}
			for H in O:
				if H and H!=5:B[H]=B.get(H,0)+1
			if B:
				K=max(B.values());P=[A for(A,B)in B.items()if B==K]
				if len(P)>1:L=min(B)if K>1 else sorted(B)[len(B)//2]
			else:L=0
			for Q in range(F,F+E):
				for R in range(G,G+E):J[Q][R]=L
	return J