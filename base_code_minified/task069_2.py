def p(g):
	A,B=len(g),len(g[0]);D={}
	for K in range(A):
		for L in range(B):
			C=g[K][L]
			if C:D[C]=D.get(C,0)+1
	H=max(D,key=D.get);E=[(A,D,g[A][D])for A in range(A)for D in range(B)if(C:=g[A][D])and C!=H];M=min(A for(A,B,C)in E);N=min(A for(B,A,C)in E);I=[(A-M,B-N,C)for(A,B,C)in E];J=[[0]*B for A in range(A)]
	for F in range(A):
		for G in range(B):
			if all(0<=F+C<A and 0<=G+D<B and g[F+C][G+D]==H for(C,D,E)in I):
				for(O,P,Q)in I:J[F+O][G+P]=Q
	return J