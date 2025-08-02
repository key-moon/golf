def p(A):
	G={}
	for H in A:
		for B in H:
			if B:G[B]=G.get(B,0)+1
	R=min(G,key=lambda F:G[F])
	for(I,H)in enumerate(A):
		for(J,B)in enumerate(H):
			if B==R:break
		else:continue
		break
	K={(I,J)};L=[(I,J)];M,N=len(A),len(A[0])
	while L:
		C,D=L.pop()
		for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
			E,F=C+O,D+P
			if 0<=E<M and 0<=F<N and A[E][F]and(E,F)not in K:K.add((E,F));L.append((E,F))
	Q=[(B-I,C-J,A[B][C])for(B,C)in K]
	for C in range(M):
		for D in range(N):
			if all(0<=C+B<M and 0<=D+E<N and A[C+B][D+E]in(0,F)for(B,E,F)in Q):
				for(O,P,S)in Q:A[C+O][D+P]=S
	return A