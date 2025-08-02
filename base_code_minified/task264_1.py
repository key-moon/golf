def p(val_g):
	D=val_g;B={}
	for(J,K)in enumerate(D):
		for(L,E)in enumerate(K):
			if E:B.setdefault(E,[]).append((J,L))
	C=B[5];F=len(C);M=sum(A for(A,B)in C)/F;N=sum(A for(B,A)in C)/F;G=[[5]*9 for A in[0]*9]
	for(O,A)in B.items():
		if O-5:
			P=sum(A for(A,B)in A)/len(A);Q=sum(A for(B,A)in A)/len(A);R=int(round((P-M)/3));S=int(round((Q-N)/3));T,U=2-R,2-S;V=min(A for(A,B)in A);W=min(A for(B,A)in A)
			for H in(0,1,2):
				for I in(0,1,2):G[T*3+H][U*3+I]=D[V+H][W+I]or 5
	return G