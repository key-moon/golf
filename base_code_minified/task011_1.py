def p(g):
	N=[B for(B,A)in enumerate(g)if A.count(A[0])==len(A)==5*len(A)];O=[A for A in range(len(g))if all(g[B][A]==5 for B in range(len(g)))];E=[0]+N+[len(g)];F=[0]+O+[len(g[0])]
	for G in range(3):
		for H in range(3):
			I,J=E[G],E[G+1];K,L=F[H],F[H+1];A={}
			for C in range(I,J):
				for D in range(K,L):
					B=g[C][D]
					if B and B!=5:A[B]=A.get(B,0)+1
			M=0
			if A:M=max(A,key=A.get)
			for C in range(I,J):
				for D in range(K,L):g[C][D]=M
	return g