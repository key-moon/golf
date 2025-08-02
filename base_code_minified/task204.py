def p(g):
	H,G=len(g),len(g[0]);E=[[0]*G for A in g];O=(1,0),(-1,0),(0,1),(0,-1);S=[(A,B)for A in range(H)for B in(0,G-1)]+[(B,A)for A in range(G)for B in(0,H-1)]
	for(C,D)in S:
		if g[C][D]==0 and not E[C][D]:
			F=[(C,D)];E[C][D]=1
			while F:
				I,J=F.pop()
				for(K,L)in O:
					A,B=I+K,J+L
					if 0<=A<H and 0<=B<G and g[A][B]==0 and not E[A][B]:E[A][B]=1;F.append((A,B))
	for C in range(H):
		for D in range(G):
			if g[C][D]==0 and not E[C][D]:
				F=[(C,D)];E[C][D]=1;P=[(C,D)];Q=C;R=C;M=D;N=D
				while F:
					I,J=F.pop()
					for(K,L)in O:
						A,B=I+K,J+L
						if 0<=A<H and 0<=B<G and g[A][B]==0 and not E[A][B]:E[A][B]=1;F.append((A,B));P.append((A,B));Q=min(Q,A);R=max(R,A);M=min(M,B);N=max(N,B)
				T=7 if(N-M+1)%2 else 2
				for(I,J)in P:g[I][J]=T
	return g