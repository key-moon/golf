def p(A):
	O,L=len(A),len(A[0]);F=[[0]*L for A in A];M=[]
	for G in range(O):
		for H in range(L):
			if A[G][H]and not F[G][H]:
				I=[(G,H)];F[G][H]=1
				for(B,C)in I:
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=B+T,C+U
						if 0<=D<O and 0<=E<L and A[D][E]and not F[D][E]:F[D][E]=1;I.append((D,E))
				M.append((I,[A[B][C]for(B,C)in I]))
	if len(M)!=2:return A
	(J,V),(K,W)=M;P=min(A for(A,B)in J);Q=min(A for(B,A)in J);R=min(A for(A,B)in K);S=min(A for(B,A)in K)
	for(B,C)in J:A[B][C]=0
	for(B,C)in K:A[B][C]=0
	for((B,C),N)in zip(J,V):A[R+(B-P)][S+(C-Q)]=N
	for((B,C),N)in zip(K,W):A[P+(B-R)][Q+(C-S)]=N
	return A