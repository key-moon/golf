def p(g):
	F=max(A.count(8)for A in g);A=[A for(A,B)in enumerate(g)if B.count(8)==F]
	for(C,B)in enumerate(g):
		if any(A==8 for A in B):
			D=A[C%2]if len(A)>1 else A[0]
			if C>D:
				for(E,G)in enumerate(B):
					if G==0 and g[D][E]==8:B[E]=1
	return g