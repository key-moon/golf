def p(val_g):
	A=val_g;B=max(map(max,A));C=[A for(A,C)in enumerate(A)for D in C if D==B];D=[C for A in A for(C,D)in enumerate(A)if D==B];E,F,G,H=min(C),max(C),min(D),max(D);J=[(E,F,G,H),(2-F,2-E,2-H,2-G)];I=[[0]*9 for A in[0]*9]
	for(K,L,M,N)in J:
		for O in range(K*4,(L+1)*4):
			for P in range(M*4,(N+1)*4):I[O][P]=B
	return I