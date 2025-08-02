def p(val_g):
	B=val_g;D={}
	for J in B:
		for G in J:
			if G:D[G]=D.get(G,0)+1
	C=max(D,key=D.get);K=sorted({A for(A,B)in enumerate(B)for D in B if D==C});L=sorted({B for A in B for(B,D)in enumerate(A)if D==C});E=[];A=[]
	for H in K:
		if A and H-A[-1]>1:E+=[A];A=[]
		A+=H,
	E+=[A];F=[];A=[]
	for I in L:
		if A and I-A[-1]>1:F+=[A];A=[]
		A+=I,
	F+=[A];M=min(B for(B,D)in enumerate(B)for A in D if A and A!=C);N=max(B for(B,D)in enumerate(B)for A in D if A and A!=C);O=min(D for B in B for(D,A)in enumerate(B)if A and A!=C);P=max(D for B in B for(D,A)in enumerate(B)if A and A!=C);Q=[A[O:P+1]for A in B[M:N+1]];return[[Q[A][D]if any(B[A][E]==C for A in E[A]for E in F[D])else 0 for D in range(len(F))]for A in range(len(E))]