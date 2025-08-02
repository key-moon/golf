def p(A):
	B={}
	for(T,U)in enumerate(A):
		for(V,C)in enumerate(U):B.setdefault(C,[]).append((T,V))
	F=G=H=I=J=K=0
	for(C,D)in B.items():
		L=[A for(A,B)in D];M=[A for(B,A)in D];N,O=min(L),max(L);P,Q=min(M),max(M);E=(O-N+1)*(Q-P+1)
		if E==len(D)and E>F:F=E;G=C;H,Y=N;I=O;J,Z=P;K=Q
	W=sorted([(len(B),A)for(A,B)in B.items()],reverse=1);X=W[1][1];R=I-H+1;S=K-J+1;return[[G if min(A,B,R-1-A,S-1-B)%2==0 else X for B in range(S)]for A in range(R)]