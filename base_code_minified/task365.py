def p(g):
	for(E,D)in enumerate(g):
		for A in range(len(D)):
			if D[A]and(E<1 or not g[E-1][A])and(A<1 or not D[A-1]):
				B=A
				while B<len(D)and D[B]:B+=1
				C=E
				while C<len(g)and all(g[C][A]for A in range(A,B)):C+=1
				if(C==len(g)or all(not g[C][A]for A in range(A,B)))and(B==len(D)or all(not g[A][B]for A in range(E,C))):return[g[C][A:B]for C in range(E,C)]
	return g