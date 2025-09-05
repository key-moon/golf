def	p(g):
	N,K=len(g),len(g[0]);J=[[0]*K	for	_	in	g]
	for	A	in	range(N):
		for	B	in	range(K):
			if	g[A][B]and	not	J[A][B]:
				C=g[A][B];L=[(A,B)];J[A][B]=1;M=[]
				while	L:
					x,y=L.pop();M.append((x,y))
					for(Q,R)in(1,0),(-1,0),(0,1),(0,-1):
						D,E=x+Q,y+R
						if	0<=D<N	and	0<=E<K	and	not	J[D][E]and	g[D][E]==C:J[D][E]=1;L.append((D,E))
				O=[p[0]for	p	in	M];P=[p[1]for	p	in	M];F,G,H,I=min(O),max(O),min(P),max(P)
				if	G-F>1and	I-H>1and	all(g[F][k]==C	for	k	in	range(H,I+1))and	all(g[G][k]==C	for	k	in	range(H,I+1))and	all(g[k][H]==C	for	k	in	range(F,G+1))and	all(g[k][I]==C	for	k	in	range(F,G+1)):
					for	x	in	range(F+1,G):
						for	y	in	range(H+1,I):g[x][y]=2
	return	g