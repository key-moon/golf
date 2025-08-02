import collections
def p(g):
	F,G=len(g),len(g[0]);E=[[0]*G for A in range(F)];N=[]
	for A in range(F):
		for B in range(G):
			if g[A][B]==5:N.append((A,B));E[A][B]=1
	O=N[:]
	for(J,K)in O:
		for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
			C,D=J+L,K+M
			if 0<=C<F and 0<=D<G and not E[C][D]and g[C][D]==5:E[C][D]=1;O.append((C,D))
	P=collections.defaultdict(list)
	for A in range(F):
		for B in range(G):
			H=g[A][B]
			if H and H!=5 and not E[A][B]:
				I=[(A,B)];E[A][B]=1
				for(J,K)in I:
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=J+L,K+M
						if 0<=C<F and 0<=D<G and not E[C][D]and g[C][D]==H:E[C][D]=1;I.append((C,D))
				S=min(A for(A,B)in I);T=min(A for(B,A)in I);Q=tuple(sorted((A-S,B-T)for(A,B)in I));P[Q].append(H)
	for(Q,R)in P.items():
		if len(R)==2:
			H=max(R)
			for A in range(F):
				for B in range(G):
					if g[A][B]==H:g[A][B]=5
			return g
	return g