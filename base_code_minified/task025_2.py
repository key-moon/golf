def p(g):
	C,D=len(g),len(g[0]);I=[(A,g[A][0])for A in range(C)if g[A][0]and g[A].count(g[A][0])==D];J=[(A,g[0][A])for A in range(D)if g[0][A]and sum(g[B][A]==g[0][A]for B in range(C))==C];E=[[0]*D for A in range(C)]
	for(B,A)in I:E[B]=[A]*D
	for(F,A)in J:
		for B in range(C):E[B][F]=A
	for B in range(C):
		for F in range(D):
			G=g[B][F]
			if not G:continue
			for(H,A)in I:
				if G==A and B!=H:E[H+(-1 if B<H else 1)][F]=A
			for(K,A)in J:
				if G==A and F!=K:E[B][K+1]=A
	return E