def p(A):
	B={}
	for H in A:
		for N in H:B[N]=B.get(N,0)+1
	C=sorted(B);O=C[0];I=C[-1];P=O if B[O]>B[I]else I;Q=C[1]if P==I else C[-2];R=set(C)-{P,Q};J,K=len(A),len(A[0]);D,L,E,M=J,-1,K,-1
	for F in range(J):
		for G in range(K):
			if A[F][G]in R:D=min(D,F);L=max(L,F);E=min(E,G);M=max(M,G)
	S,H=L-D+1,M-E+1;T=[(B,C,A[D+B][E+C])for B in range(S)for C in range(H)if A[D+B][E+C]in R]
	for U in range(J-S+1):
		for V in range(K-H+1):
			if all(A[U+B][V+C]==Q for(B,C,D)in T):
				for(F,G,W)in T:A[U+F][V+G]=W
	return A