def p(g):
	for E in range(1,len(g)-1):
		F,B,G=g[E-1],g[E],g[E+1];A=-1
		for C in range(len(B)):
			if B[C]and F[C]==B[C]==G[C]:
				if A<0:A=C
			elif A>=0:
				for D in range(C-A):
					if D&1:B[A+D]=0
				A=-1
		if A>=0:
			for D in range(len(B)-A):
				if D&1:B[A+D]=0
	return g