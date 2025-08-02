def p(g):
	C={}
	for(B,L)in enumerate(g):
		for(D,G)in enumerate(L):
			A=C.get(G)
			if A:A[0]=min(A[0],B);A[1]=max(A[1],B);A[2]=min(A[2],D);A[3]=max(A[3],D);A[4]+=1
			else:C[G]=[B,B,D,D,1]
	H=max(C,key=lambda c:C[c][4]);I=max((A for A in C if A!=H),key=lambda c:C[c][4]);J,K,M,N,O=C[I]
	for(E,A)in C.items():
		if E!=H and E!=I:
			B,D=A[0],A[2]
			if B<J or B>K:
				for F in range(min(B,J),max(B,K)+1):g[F][D]=E
			else:
				for F in range(min(D,M),max(D,N)+1):g[B][F]=E
	return g