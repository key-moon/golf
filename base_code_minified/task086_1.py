def p(g):
	Q,R=len(g),len(g[0]);I=[A[:]for A in g];G=set()
	for C in range(Q):
		for D in range(R):
			if g[C][D]and(C,D)not in G:
				J=g[C][D];H=[(C,D)];G.add((C,D))
				for S in H:
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=S[0]+T,S[1]+U
						if 0<=A<Q and 0<=B<R and g[A][B]==J and(A,B)not in G:G.add((A,B));H.append((A,B))
				E=[A[0]for A in H];F=[A[1]for A in H];K,L=min(E)-1,max(E)+1;M,N=min(F)-1,max(F)+1;O=[]
				for A in range(K+1,L):
					for B in range(M+1,N):
						P=g[A][B]
						if P and P!=J:O.append((A,B));V=P
				E=[A[0]for A in O];F=[A[1]for A in O];W,X=min(E)-1,max(E)+1;Y,Z=min(F)-1,max(F)+1
				for A in range(K,L+1):
					for B in range(M,N+1):
						if A in(K,L)or B in(M,N):I[A][B]=J
				for A in range(W,X+1):
					for B in range(Y,Z+1):I[A][B]=V
	return I