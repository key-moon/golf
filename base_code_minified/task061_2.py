def p(val_g):
	F=val_g;import math
	for D in F:
		E={};B=0
		for(C,A)in enumerate(D):
			if A:
				if A in E:B=math.gcd(B,C-E[A])
				E[A]=C
		if not B:B=len(E)
		G=[0]*B
		for(C,A)in enumerate(D):
			if A:G[C%B]=A
		for(C,A)in enumerate(D):
			if not A:D[C]=G[C%B]
	return F