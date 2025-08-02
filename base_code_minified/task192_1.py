def p(g):
	J=sum(g,[]);K=set(J)-{0};F=max(K,key=J.count);D,E=len(g),len(g[0]);A=[[F if g[A][B]==F else-1 for B in range(E)]for A in range(D)];G=[(C,B)for B in range(E)for C in(0,D-1)if A[C][B]==-1]+[(B,C)for B in range(D)for C in(0,E-1)if A[B][C]==-1]
	while G:
		B,C=G.pop();A[B][C]=-2
		for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
			H,I=B+L,C+M
			if 0<=H<D and 0<=I<E and A[H][I]==-1:G.append((H,I))
	for B in range(D):
		for C in range(E):
			if A[B][C]==-1:A[B][C]=F
			elif A[B][C]==-2:A[B][C]=0
	return A