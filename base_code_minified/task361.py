def p(g):
	A=[(A,B)for A in range(10)for B in range(10)if g[A][B]];H,I=min(A)[0],max(A)[0];J,K=min(A,key=lambda x:x[1])[1],max(A,key=lambda x:x[1])[1];D=H+I;E=J+K
	for(F,G)in A:
		L=g[F][G];B=2*F-D;C=2*G-E
		for(M,N)in((C,-B),(-B,-C),(-C,B)):g[(D+M)//2][(E+N)//2]=L
	return g