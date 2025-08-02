def p(A):
	B=range;k={A for B in A for A in B if A};F,G=sorted(k,key=lambda E:max(A for B in A for A in B if A==E)/min(A for B in A for A in B if A==E)if False else 0)
	def Y(A):B=[B for(B,C)in enumerate(E)for(E,D)in enumerate(C)if D==A];C=[C for(E,B)in enumerate(E)for(C,D)in enumerate(B)if D==A];return min(B),max(B),min(C),max(C)
	H,I,J,K=Y(F);L=I-H+1;M=K-J+1;N,O,P,Q=Y(G);R=O-N+1;S=Q-P+1
	if M*R>=L*S:Z,l,m,a,b,T,E=F,H,I,J,K,L,M;c,d,e,n,o,f,U=G,N,O,P,Q,R,S
	else:Z,l,m,a,b,T,E=G,N,O,P,Q,R,S;c,d,e,n,o,f,U=F,H,I,J,K,L,M
	V=E+f;W=T+U;g=(d+e)//2;h=(a+b)//2;X=[[3]*10 for A in B(10)];i=(T-1)//2
	for p in B(-i,i+1):
		C=g+p
		if 0<=C<10:
			for q in B(-V//2,V-V//2):
				D=h+q
				if 0<=D<10:X[C][D]=Z
	j=(U-1)//2
	for r in B(-j,j+1):
		D=h+r
		if 0<=D<10:
			for s in B(-W//2,W-W//2):
				C=g+s
				if 0<=C<10:X[C][D]=c
	return X