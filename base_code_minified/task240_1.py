def p(g):
	import math as H;I,F=len(g),len(g[0]);G=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];A=sorted({A for(A,B,B)in G});B=sorted({B for(A,B,A)in G})
	if len(A)>1:
		D=A[1]-A[0]
		for C in range(2,len(A)):D=H.gcd(D,A[C]-A[C-1])
	else:D=I-1-A[0]
	if len(B)>1:
		E=B[1]-B[0]
		for C in range(2,len(B)):E=H.gcd(E,B[C]-B[C-1])
	else:E=F-1-B[0]
	J=[[0]*F for A in g]
	for(K,L,M)in G:
		for C in range(K,I,D):
			for N in range(L,F,E):J[C][N]=M
	return J