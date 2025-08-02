def p(g):
	B=len(g);D=len(g[0])
	for A in range(B):
		if g[A][0]and all(B==g[A][0]for B in g[A]):I=g[A][0];break
	J=[A for A in range(B)if all(A==I for A in g[A])];K=[A for A in range(D)if all(g[B][A]==I for B in range(B))];G=[-1]*B
	for A in range(len(J)-1):
		for S in range(J[A]+1,J[A+1]):G[S]=A
	H=[-1]*D
	for A in range(len(K)-1):
		for T in range(K[A]+1,K[A+1]):H[T]=A
	C=[(G[A],H[B],g[A][B])for A in range(B)for B in range(D)if g[A][B]!=0 and g[A][B]!=I]
	for L in{A[0]for A in C}:
		E=[A[2]for A in C if A[0]==L]
		if len({*E})==1:
			M=E[0];Q=[A[1]for A in C if A[0]==L];N,O=min(Q),max(Q)
			for A in range(B):
				if G[A]==L:
					for F in range(D):
						if N<=H[F]<=O:g[A][F]=M
	for P in{A[1]for A in C}:
		E=[A[2]for A in C if A[1]==P]
		if len({*E})==1:
			M=E[0];R=[A[0]for A in C if A[1]==P];N,O=min(R),max(R)
			for F in range(D):
				if H[F]==P:
					for A in range(B):
						if N<=G[A]<=O:g[A][F]=M
	return g