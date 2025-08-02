def p(A):
	C,E=len(A),len(A[0]);D=[(B,C)for B in range(C)for C in range(E)if A[B][C]==0];F=min(A for(A,B)in D);H=min(A for(B,A)in D);G=max(A for(A,B)in D)-F+1
	for B in range(1,C+1):
		if all(A[C][D]==A[C%B][D%B]for C in range(C)for D in range(E)if A[C][D]):break
	return[[A[(F+C)%B][(H+D)%B]for D in range(G)]for C in range(G)]