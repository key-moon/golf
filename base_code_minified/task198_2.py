def p(g):
	F,I=len(g),len(g[0]);O=next(A for B in g for A in B if A);G=[A for A in range(F)if g[A].count(O)>I/2];H=[A for A in range(I)if sum(g[B][A]==O for B in range(F))>F/2];K=[-1]+G+[F];L=[-1]+H+[I];M,C=len(K)-1,len(L)-1;N=list(range(M*C))
	def J(x):
		while N[x]!=x:x=N[x]
		return x
	def P(a,b):
		a,b=J(a),J(b)
		if a!=b:N[a]=b
	for D in G:
		A=sum(1 for A in G if A<D)
		for E in range(I):
			if g[D][E]==0 and E not in H:B=sum(1 for A in H if A<E);P(A*C+B,(A+1)*C+B)
	for E in H:
		B=sum(1 for A in H if A<E)
		for D in range(F):
			if g[D][E]==0 and D not in G:A=sum(1 for A in G if A<D);P(A*C+B,A*C+B+1)
	from collections import Counter as Q;R=Q(J(A)for A in range(M*C));S=R.most_common(1)[0][0]
	for A in range(M):
		for B in range(C):
			T=4 if J(A*C+B)==S else 3
			for D in range(K[A]+1,K[A+1]):
				for E in range(L[B]+1,L[B+1]):g[D][E]=T
	return g