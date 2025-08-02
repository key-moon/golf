def p(g):
	A=0
	while A<len(g):
		C=next(A for A in g[A]if A);B=A
		while B<len(g)and next(A for A in g[B]if A)==C:B+=1
		D={B for A in g[A:B]for(B,C)in enumerate(A)if C<1}
		for E in g[A:B]:
			for F in D:E[F]=0
		A=B
	return g