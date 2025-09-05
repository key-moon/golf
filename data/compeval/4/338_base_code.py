def	p(g):
	L,G=len(g),len(g[0]);M=[[0]*G	for	_	in	g];H=[[0]*G	for	_	in	g]
	for	I	in	range(L):
		for	J	in	range(G):
			if	g[I][J]==2and	not	H[I][J]:
				K=[(I,J)];H[I][J]=1
				for(P,Q)in	K:
					for(R,S)in(1,0),(-1,0),(0,1),(0,-1):
						A,B=P+R,Q+S
						if	0<=A<L	and	0<=B<G	and	g[A][B]==2and	not	H[A][B]:H[A][B]=1;K.append((A,B))
				N=[A[0]for	A	in	K];O=[A[1]for	A	in	K];C,D,E,F=min(N),max(N),min(O),max(O)
				if	D-C>1and	F-E>1and	all(g[C][A]==2for	A	in	range(E,F+1))and	all(g[D][A]==2for	A	in	range(E,F+1))and	all(g[A][E]==2for	A	in	range(C,D+1))and	all(g[A][F]==2for	A	in	range(C,D+1)):
					for	A	in	range(C+1,D):
						for	B	in	range(E+1,F):M[A][B]=3
	return	M