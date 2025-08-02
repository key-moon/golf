def p(g):
	G,D=len(g),len(g[0]);E,F,J,K=D,G,0,0
	for A in range(G):
		for B in range(D):
			if g[A][B]==5:
				if A<E:E=A
				if B<F:F=B
				if A>J:J=A
				if B>K:K=B
	R={(A-E-1,B-F-1)for A in range(E+1,J)for B in range(F+1,K)if g[A][B]not in(0,5)};S=next(iter(R));T=g[E+1+S[0]][F+1+S[1]];L=[[0]*D for A in g]
	for A in range(G):
		for B in range(D):
			O=g[A][B]
			if O and O!=5 and not L[A][B]:
				C=[(A,B)];L[A][B]=1
				for U in range(len(C)):
					V,W=C[U]
					for(X,Y)in((1,0),(-1,0),(0,1),(0,-1)):
						H,I=V+X,W+Y
						if 0<=H<G and 0<=I<D and not L[H][I]and g[H][I]==O:L[H][I]=1;C.append((H,I))
				Z,a=C[0]
				if not(E<Z<J and F<a<K):
					P,Q=G,D
					for(M,N)in C:
						if M<P:P=M
						if N<Q:Q=N
					if{(A-P,B-Q)for(A,B)in C}==R:
						for(M,N)in C:g[M][N]=T
	return g