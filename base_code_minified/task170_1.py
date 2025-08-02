def p(A):
	B={}
	for(P,Q)in enumerate(A):
		for(R,I)in enumerate(Q):
			if I:B.setdefault(I,[]).append((P,R))
	J=sorted(B,key=lambda H:-len(B[H]));K,S=J[0],J[1];C,D=B[K],B[S];E,T=min(A for(A,B)in C),max(A for(A,B)in C);F,U=min(A for(B,A)in C),max(A for(B,A)in C);L,V=min(A for(A,B)in D),max(A for(A,B)in D);M,W=min(A for(B,A)in D),max(A for(B,A)in D);G,H=V-L+1,W-M+1;N,O=(T-E+1)//G,(U-F+1)//H;X=[[any(A[B][D]==K for B in range(E+B*N,E+(B+1)*N)for D in range(F+C*O,F+(C+1)*O))for C in range(H)]for B in range(G)];return[[A[L+B][M+C]*X[B][C]for C in range(H)]for B in range(G)]