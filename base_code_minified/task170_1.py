def p(g):
	A={}
	for(O,P)in enumerate(g):
		for(Q,H)in enumerate(P):
			if H:A.setdefault(H,[]).append((O,Q))
	I=sorted(A,key=lambda c:-len(A[c]));J,R=I[0],I[1];B,C=A[J],A[R];D,S=min(A for(A,B)in B),max(A for(A,B)in B);E,T=min(A for(B,A)in B),max(A for(B,A)in B);K,U=min(A for(A,B)in C),max(A for(A,B)in C);L,V=min(A for(B,A)in C),max(A for(B,A)in C);F,G=U-K+1,V-L+1;M,N=(S-D+1)//F,(T-E+1)//G;W=[[any(g[A][C]==J for A in range(D+A*M,D+(A+1)*M)for C in range(E+B*N,E+(B+1)*N))for B in range(G)]for A in range(F)];return[[g[K+A][L+B]*W[A][B]for B in range(G)]for A in range(F)]