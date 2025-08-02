def p(A):
	P,Q=len(A),len(A[0]);E={}
	for(B,R)in enumerate(A):
		for(C,F)in enumerate(R):
			if F:E.setdefault(F,[]).append((B,C))
	for(S,D)in E.items():
		G=[A for(A,B)in D];H=[A for(B,A)in D];I=max(G)-min(G)+1;J=max(H)-min(H)+1
		for(K,L)in((-I,0),(I,0),(0,-J),(0,J)):
			M=1
			for(B,C)in D:
				N,O=B+K,C+L
				if not(0<=N<P and 0<=O<Q and A[N][O]==0):M=0;break
			if M:
				for(B,C)in D:A[B+K][C+L]=S
	return A