def p(g):
	E,F=len(g),len(g[0]);G=0;H=I=J=K=0
	for A in range(E):
		for C in range(A+1,E+1):
			for B in range(F):
				for D in range(B+1,F+1):
					if(C-A)*(D-B)>G and all(not g[A][C]for A in range(A,C)for C in range(B,D)):G=(C-A)*(D-B);H=A;I=C;J=B;K=D
	for L in range(H,I):
		for M in range(J,K):g[L][M]=6
	return g