def p(g):
	B,D=len(g),len(g[0]);C=[(A,B)for A in range(B)for B in range(D)if g[A][B]==0];E=min(A for(A,B)in C);G=min(A for(B,A)in C);F=max(A for(A,B)in C)-E+1
	for A in range(1,B+1):
		if all(g[B][C]==g[B%A][C%A]for B in range(B)for C in range(D)if g[B][C]):break
	return[[g[(E+B)%A][(G+C)%A]for C in range(F)]for B in range(F)]