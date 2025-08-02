def p(g):
	C=list(zip(*g));C=[A for A in C if 5 not in A];A=[list(A)for A in zip(*C)];F=len(A);G=len(A[0])
	for D in range(F):
		for B in range(G):
			if A[D][B]==0:
				for H in(1,-1):
					E=D+H
					if 0<=E<F and A[E][B]!=0:A[D][B]=A[E][B];break
	return A