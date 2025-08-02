def p(g):
	G,H=len(g),len(g[0]);C=set();I=[]
	for D in range(G):
		for E in range(H):
			if g[D][E]and(D,E)not in C:
				F=[(D,E)];C.add((D,E))
				for J in F:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=J[0]+M,J[1]+N
						if 0<=A<G and 0<=B<H and g[A][B]and(A,B)not in C:C.add((A,B));F.append((A,B))
				I.append(F)
	O=max(I,key=lambda r:(len(r),max(r)[0]));K,L=zip(*O);return[[g[A][B]for B in range(min(L),max(L)+1)]for A in range(min(K),max(K)+1)]