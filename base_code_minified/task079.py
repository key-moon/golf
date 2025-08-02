def p(A):
	D={}
	for E in range(len(A)-2):
		for F in range(len(A[0])-2):
			G={A[E+B][F+C]for B in range(3)for C in range(3)if A[E+B][F+C]}
			if len(G)==1:B=G.pop();C=tuple((C,D)for C in range(3)for D in range(3)if A[E+C][F+D]==B);D[B,C]=D.get((B,C),0)+1
	(B,C),H=max(D.items(),key=lambda K:(K[1],K[0][0]));return[[B if(A,D)in C else 0 for D in range(3)]for A in range(3)]