def p(g):
	A=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==2];H=min(A for(A,B)in A);K=min(A for(B,A)in A);D=max(A for(A,B)in A)-H+1;E=[[0]*D for A in range(D)]
	for(F,G)in A:E[F-H][G-K]=2
	I=next(A for B in g for A in B if A*(A-2));B=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==I];J=min(A for(A,B)in B);L=min(A for(B,A)in B);C=(D-2)//(max(A for(A,B)in B)-J+1)
	for(F,G)in B:
		for M in range(C):
			for N in range(C):E[1+(F-J)*C+M][1+(G-L)*C+N]=I
	return E