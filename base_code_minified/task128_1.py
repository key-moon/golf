def p(A):
	F=len(A);H={}
	for(S,T)in enumerate(A):
		for(U,I)in enumerate(T):
			if I:H.setdefault(I,[]).append((S,U))
	C=[]
	for(B,J)in H.items():K=[A for(A,B)in J];L=[A for(B,A)in J];C.append((B,min(K),max(K),min(L),max(L)))
	C.sort(key=lambda N:N[0]);V=sum(A[2]-A[1]+1 for A in C);M=0;N={}
	for(B,D,G,E,O)in reversed(C):N[B]=F-V+M;M+=G-D+1
	P=[[0]*F for A in range(F)]
	for(B,D,G,E,O)in C:
		W=G-D+1;X=O-E+1;Y=N[B]
		for Q in range(W):
			for R in range(X):
				if A[D+Q][E+R]==B:P[Y+Q][E+R]=B
	return P