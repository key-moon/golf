def p(A):
	I,H=len(A),len(A[0]);F=[[0]*H for A in A];P=(1,0),(-1,0),(0,1),(0,-1);T=[(A,B)for A in range(I)for B in(0,H-1)]+[(B,A)for A in range(H)for B in(0,I-1)]
	for(D,E)in T:
		if A[D][E]==0 and not F[D][E]:
			G=[(D,E)];F[D][E]=1
			while G:
				J,K=G.pop()
				for(L,M)in P:
					B,C=J+L,K+M
					if 0<=B<I and 0<=C<H and A[B][C]==0 and not F[B][C]:F[B][C]=1;G.append((B,C))
	for D in range(I):
		for E in range(H):
			if A[D][E]==0 and not F[D][E]:
				G=[(D,E)];F[D][E]=1;Q=[(D,E)];R=D;S=D;N=E;O=E
				while G:
					J,K=G.pop()
					for(L,M)in P:
						B,C=J+L,K+M
						if 0<=B<I and 0<=C<H and A[B][C]==0 and not F[B][C]:F[B][C]=1;G.append((B,C));Q.append((B,C));R=min(R,B);S=max(S,B);N=min(N,C);O=max(O,C)
				U=7 if(O-N+1)%2 else 2
				for(J,K)in Q:A[J][K]=U
	return A