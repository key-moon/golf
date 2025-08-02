def p(g):
	F=[A for(A,B)in enumerate(g)if len(set(B))==1];G=[A for A in range(len(g[0]))if len({g[B][A]for B in range(len(g))})==1];A=[0]+F+[len(g)];C=[0]+G+[len(g[0])];H=[[[A[C[D]:C[D+1]]for A in g[A[B]:A[B+1]]]for D in range(len(C)-1)]for B in range(len(A)-1)];K=list(map(list,zip(*H)));D=[]
	for B in val_bt:
		for I in range(len(B[0])):
			E=[]
			for J in B:E+=J[I]
			D.append(E)
		if A[val_bt.index(B)+1]<len(g):D.append(g[A[val_bt.index(B)+1]])
	return D