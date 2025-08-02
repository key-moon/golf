def p(g):
	J,K=len(g),len(g[0]);E=set();F=()
	for C in range(J):
		for D in range(K):
			if not g[C][D]and(C,D)not in E:
				L=[(C,D)];G={(C,D)};E.add((C,D))
				for(H,I)in L:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=H+M,I+N
						if 0<=A<J and 0<=B<K and not g[A][B]and(A,B)not in E:E.add((A,B));G.add((A,B));L.append((A,B))
				if len(G)>len(F):F=G
	for(H,I)in F:g[H][I]=1
	return g