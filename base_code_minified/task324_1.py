def p(val_g):
	A=val_g;M=len(A);N=len(A[0]);E=[[0]*N for A in range(M)]
	for F in range(M):
		for G in range(N):
			if not E[F][G]:
				H=A[F][G];E[F][G]=1;D=[(G,F)]
				for T in range(len(D)):
					I,J=D[T]
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=I+U,J+V
						if 0<=B<N and 0<=C<M and not E[C][B]and A[C][B]==H:E[C][B]=1;D.append((B,C))
				O=[A for(A,B)in D];P=[A for(B,A)in D];I,B,J,C=min(O),max(O),min(P),max(P);Q=[(D,C)for C in range(J,C+1)for D in range(I,B+1)if A[C][D]!=H]
				if len(Q)==1:
					K,L=Q[0];W=A[L][K]
					for X in(0,1):
						for Y in(0,1):
							R=I+B-K if X else K;S=J+C-L if Y else L
							if A[S][R]==H:A[S][R]=W
					A[L][K]=H
	return A