def p(A):
	M={A for B in A for A in B if A};F=[]
	for C in M:G=[A for(A,B)in enumerate(A)for(E,D)in enumerate(B)if D==C];H=[B for(E,A)in enumerate(A)for(B,D)in enumerate(A)if D==C];F.append((C,min(G),max(G),min(H),max(H)))
	N,O=sorted(F,key=lambda M:M[4]-M[3]-(M[2]-M[1]),reverse=True);P,I,B,J,K=N;Q,T,U,L,V=O
	for D in range(I,B+1):
		for E in range(J,K+1):A[D][E]=P
	R,S=B-I+1,K-J+1
	for D in range(B+1,B+1+R):
		for E in range(L,L+S):A[D][E]=Q
	return A