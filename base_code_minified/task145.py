def p(g):
	F,E=len(g),len(g[0]);from collections import deque;G=[[0]*E for A in g];H=deque()
	for A in range(F):
		for B in range(E):
			if g[A][B]==0 and(A==0 or B==0 or A==F-1 or B==E-1):G[A][B]=1;H.append((A,B))
	while H:
		A,B=H.popleft()
		for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
			C,D=A+I,B+J
			if 0<=C<F and 0<=D<E and g[C][D]==0 and not G[C][D]:G[C][D]=1;H.append((C,D))
	for A in range(F):
		for B in range(E):
			if g[A][B]==0 and not G[A][B]:g[A][B]=1
	for A in range(F):
		for B in range(E):
			if g[A][B]==0:
				for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
					C,D=A+I,B+J
					if 0<=C<F and 0<=D<E and g[C][D]==2:g[A][B]=8;break
	return g