def p(A):
	H={}
	for(B,L)in enumerate(A):
		for(C,F)in enumerate(L):
			if F:H.setdefault(F,[]).append((B,C))
	M,N=len(A),len(A[0])
	for(F,D)in H.items():
		if len(D)<2:continue
		for(K,O)in H.items():
			if K==F:continue
			G={A:[]for A in D}
			for(B,C)in O:P=min(D,key=lambda N:abs(B-N[0])+abs(C-N[1]));G[P].append((B,C))
			E=[A for A in D if G[A]]
			if len(E)==1 and len(G[E[0]])>1:
				Q,R=E[0];S=[(A-Q,B-R)for(A,B)in G[E[0]]]
				for(B,C)in D:
					if(B,C)!=E[0]:
						for(T,U)in S:
							I,J=B+T,C+U
							if 0<=I<M and 0<=J<N and A[I][J]==0:A[I][J]=K
	return A