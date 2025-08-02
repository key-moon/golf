def p(g):
	C=len(g);B=[A for(A,B)in enumerate(g)if all(A==5 for A in B)];H=[A for A in range(C)if all(g[B][A]==5 for B in range(C))];B=[-1]+B+[C];H=[-1]+H+[C];D=B[1]-B[0]-1;I=[A[:]for A in g]
	for L in range(3):
		for M in range(3):
			E=B[L]+1;F=H[M]+1;N=[g[A][B]for A in range(E,E+D)for B in range(F,F+D)];A={}
			for G in N:
				if G and G!=5:A[G]=A.get(G,0)+1
			if A:
				J=max(A.values());O=[A for(A,B)in A.items()if B==J]
				if len(O)>1:K=min(A)if J>1 else sorted(A)[len(A)//2]
			else:K=0
			for P in range(E,E+D):
				for Q in range(F,F+D):I[P][Q]=K
	return I