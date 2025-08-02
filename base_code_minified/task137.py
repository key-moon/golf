def p(g):
	B=len(g);A=[]
	for(H,I)in enumerate(g):
		for(J,N)in enumerate(I):
			if N:A.append((H,J));F=N
	C=sorted({A for(A,B)in A});D=sorted({A for(B,A)in A});G=max(C[1]-C[0],C[-1]-C[-2],D[1]-D[0],D[-1]-D[-2]);Q=C[0]%G;R=D[0]%G;S=range(Q,B,G);T=range(R,B,G);E=[[0]*B for A in range(B)]
	for I in S:E[I]=[F]*B
	for H in range(B):
		for J in T:E[H][J]=F
	A=sorted(A)
	for((O,K),(L,P))in zip(A,A[1:]):
		for M in range(min(O,L),max(O,L)+1):E[M][K]=F
		for M in range(min(K,P),max(K,P)+1):E[L][M]=F
	return E