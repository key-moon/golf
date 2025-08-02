def p(g):
	E,F=len(g),len(g[0]);G=set()
	for B in range(E):
		for A in range(F):
			C=g[B][A]
			if C:
				if B+1<E and(D:=g[B+1][A])!=C and D:G|={C,D}
				if A+1<F and(D:=g[B][A+1])!=C and D:G|={C,D}
	H=[(A,B)for A in range(E)for B in range(F)if g[A][B]in G];M=min(A for(A,B)in H);N=max(A for(A,B)in H);O=min(A for(B,A)in H);P=max(A for(B,A)in H);I=[g[A][O:P+1]for A in range(M,N+1)];J,D=len(I),len(I[0]);Q={A for B in g for A in B if A and A not in G}
	for B in range(E-J+1):
		for A in range(F-D+1):
			C=g[B][A]
			if C in Q and(B==0 or g[B-1][A]!=C)and(A==0 or g[B][A-1]!=C)and all(g[B+E][A:A+D]==[C]*D for E in range(J)):
				for K in range(J):
					for L in range(D):g[B+K][A+L]=I[K][L]
	return g