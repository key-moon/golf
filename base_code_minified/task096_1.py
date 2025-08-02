def p(g):
	C,F=len(g),len(g[0])
	for B in range(C,0,-1):
		if B&1:
			for D in range(C-B+1):
				for E in range(F-B+1):
					A=[A[E:E+B]for A in g[D:D+B]]
					if len({*sum(A,[])})>1 and A==[A[::-1]for A in A]and A==A[::-1]:return A
	return g