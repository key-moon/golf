def p(A):
	D={}
	for(C,M)in enumerate(A):
		for(E,H)in enumerate(M):
			B=D.get(H)
			if B:B[0]=min(B[0],C);B[1]=max(B[1],C);B[2]=min(B[2],E);B[3]=max(B[3],E);B[4]+=1
			else:D[H]=[C,C,E,E,1]
	I=max(D,key=lambda I:D[I][4]);J=max((A for A in D if A!=I),key=lambda I:D[I][4]);K,L,N,O,P=D[J]
	for(F,B)in D.items():
		if F!=I and F!=J:
			C,E=B[0],B[2]
			if C<K or C>L:
				for G in range(min(C,K),max(C,L)+1):A[G][E]=F
			else:
				for G in range(min(E,N),max(E,O)+1):A[C][G]=F
	return A