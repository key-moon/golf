def p(A):
	import math
	for E in A:
		F={};C=0
		for(D,B)in enumerate(E):
			if B:
				if B in F:C=math.gcd(C,D-F[B])
				F[B]=D
		if not C:C=len(F)
		G=[0]*C
		for(D,B)in enumerate(E):
			if B:G[D%C]=B
		for(D,B)in enumerate(E):
			if not B:E[D]=G[D%C]
	return A