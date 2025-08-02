def p(g):
	F,C=len(g),len(g[0]);G=0
	for B in range(F):
		for D in range(B,F):
			H=D-B+1;A=0;J=[all(not g[B][A]for B in range(B,D+1))for A in range(C)]
			for E in range(C+1):
				if E<C and J[E]:A+=1
				else:
					if A*H>G:G,K,L,M,I=A*H,B,D,A,E-A
					A=0
	for N in range(K,L+1):
		for O in range(I,I+M):g[N][O]=6
	return g