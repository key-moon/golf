def p(g):
	C=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==1];A,B=map(min,zip(*C));D,E=map(max,zip(*C));H=[(C-A,D-B)for(C,D)in C];I=[(C-A,D-B)for C in range(A,D+1)for D in range(B,E+1)if g[C][D]==4];J,K=D-A+1,E-B+1
	for F in range(len(g)-J+1):
		for G in range(len(g[0])-K+1):
			if all(g[F+A][G+B]==4 for(A,B)in I):
				for(L,M)in H:g[F+L][G+M]=1
	return g