def p(g):
	I,J=len(g),len(g[0]);F=set();M=[]
	for A in range(I):
		for B in range(J):
			if g[A][B]==9 and(A,B)not in F:
				C=[(A,B)];F.add((A,B))
				for(R,S)in C:
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=R+T,S+U
						if 0<=D<I and 0<=E<J and g[D][E]==9 and(D,E)not in F:F.add((D,E));C.append((D,E))
				M.append(C)
	C=max(M,key=len);N=[A for(A,B)in C];O=[A for(B,A)in C];K,L=min(N),min(O);G=max(N)-K+1;H=max(O)-L+1
	for A in range(I-G+1):
		for B in range(J-H+1):
			if(A,B)!=(K,L)and any(g[A+C][B+D]for C in range(G)for D in range(H))and all(g[A+C][B+D]!=9 for C in range(G)for D in range(H)):
				for P in range(G):
					for Q in range(H):g[K+P][L+Q]=g[A+P][B+Q]
				return g
	return g