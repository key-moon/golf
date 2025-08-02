def p(g):
	A=[(A,B,g[A][B])for A in range(10)for B in range(10)if g[A][B]];F=(min(A for(A,B,C)in A)+max(A for(A,B,C)in A))//2;G=(min(A for(B,A,C)in A)+max(A for(B,A,C)in A))//2
	for(B,C,H)in A:D=2*F-B;E=2*G-C;g[B][E]=g[D][C]=g[D][E]=H
	return g