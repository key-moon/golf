def p(g):
	L,G=len(g),len(g[0]);C=[[0]*G for A in g]
	for D in range(L):
		for E in range(G):
			if g[D][E]==2 and not C[D][E]:
				H=[(D,E)];I=[];C[D][E]=1
				while H:
					M,F=H.pop();I.append((M,F))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=M+P,F+Q
						if 0<=A<L and 0<=B<G and g[A][B]==2 and not C[A][B]:C[A][B]=1;H.append((A,B))
				N=[A for(A,B)in I];R,J=min(N),max(N);S=(J-R+1)//2;O=J-S+1
				for K in range(O,J+1):
					T=K-O+1;U=sorted(B for(A,B)in I if A==K)
					for F in U[:T]:g[K][F]=8
	return g