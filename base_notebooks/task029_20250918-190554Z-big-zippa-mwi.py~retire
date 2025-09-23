def p(g,L=len,E=enumerate):
	for B in set(sum(g,[])):
		G=[[D,A]for(A,C)in E(g)for(D,F)in E(C)if F==B];C=sum(G,[]);D=C[::2];F=C[1::2];A=g[min(F):max(F)];A=[A[min(D)+1:max(D)][:]for A in A]
		if A[0].count(B)==L(A[0]):return A[1:]
	return g