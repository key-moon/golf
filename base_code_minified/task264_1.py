def p(A):
	C={}
	for(J,K)in enumerate(A):
		for(L,E)in enumerate(K):
			if E:C.setdefault(E,[]).append((J,L))
	D=C[5];F=len(D);M=sum(A for(A,B)in D)/F;N=sum(A for(B,A)in D)/F;G=[[5]*9 for A in[0]*9]
	for(O,B)in C.items():
		if O-5:
			P=sum(A for(A,B)in B)/len(B);Q=sum(A for(B,A)in B)/len(B);R=int(round((P-M)/3));S=int(round((Q-N)/3));T,U=2-R,2-S;V=min(A for(A,B)in B);W=min(A for(B,A)in B)
			for H in(0,1,2):
				for I in(0,1,2):G[T*3+H][U*3+I]=A[V+H][W+I]or 5
	return G