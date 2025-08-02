def p(A):
	I,G=len(A),len(A[0]);J=[A.count(8)for A in A];K=[sum(A[B]==8 for A in A)for B in range(G)];H=max(J)>max(K);M=[A for A in(range(I)if H else range(G))if H and J[A]or not H and K[A]]
	for(C,D)in[(B,C)for B in range(I)for C in range(G)if A[B][C]==2]:
		L=(C,D)[not H];B=min(M,key=lambda N:(abs(L-N),L-N))
		if H:
			for E in range(min(C,B),max(C,B)+1):A[E][D]=2
			for E in range(B-1,B+2):
				for F in range(D-1,D+2):
					if 0<=E<I and 0<=F<G:A[E][F]=8
			A[B][D]=2
		else:
			for F in range(min(D,B),max(D,B)+1):A[C][F]=2
			for E in range(C-1,C+2):
				for F in range(B-1,B+2):
					if 0<=E<I and 0<=F<G:A[E][F]=8
			A[C][B]=2
	return A