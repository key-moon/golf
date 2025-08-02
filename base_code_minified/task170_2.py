def p(A):
	D={}
	for J in A:
		for G in J:
			if G:D[G]=D.get(G,0)+1
	C=max(D,key=D.get);K=sorted({A for(A,B)in enumerate(A)for D in B if D==C});L=sorted({B for A in A for(B,D)in enumerate(A)if D==C});E=[];B=[]
	for H in K:
		if B and H-B[-1]>1:E+=[B];B=[]
		B+=H,
	E+=[B];F=[];B=[]
	for I in L:
		if B and I-B[-1]>1:F+=[B];B=[]
		B+=I,
	F+=[B];M=min(B for(B,D)in enumerate(A)for A in D if A and A!=C);N=max(B for(B,D)in enumerate(A)for A in D if A and A!=C);O=min(D for B in A for(D,A)in enumerate(B)if A and A!=C);P=max(D for B in A for(D,A)in enumerate(B)if A and A!=C);Q=[A[O:P+1]for A in A[M:N+1]];return[[Q[B][D]if any(A[B][E]==C for B in E[B]for E in F[D])else 0 for D in range(len(F))]for B in range(len(E))]