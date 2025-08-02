def p(g):
	from collections import Counter as M,deque;C,D=len(g),len(g[0]);L=M(A for B in g for A in B if A).most_common(1)[0][0];K=[[g[A][B]==L for B in range(D)]for A in range(C)];E=[[0]*D for A in range(C)];H=deque()
	for A in range(C):
		for B in(0,D-1):
			if not K[A][B]:E[A][B]=1;H.append((A,B))
	for B in range(D):
		for A in(0,C-1):
			if not K[A][B]and not E[A][B]:E[A][B]=1;H.append((A,B))
	while H:
		F,G=H.popleft()
		for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
			I,J=F+N,G+O
			if 0<=I<C and 0<=J<D and not K[I][J]and not E[I][J]:E[I][J]=1;H.append((I,J))
	for F in range(C):
		for G in range(D):g[F][G]=L if K[F][G]or g[F][G]and not E[F][G]else 0
	return g