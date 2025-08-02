def p(g):
	K=len(g);L=len(g[0]);F=set()
	for G in range(K):
		for H in range(L):
			if g[G][H]!=8 and(G,H)not in F:
				I=[(G,H)];M=[];C={};F.add((G,H))
				while I:
					A,B=I.pop();M.append((A,B));J=g[A][B]
					if J>0 and J not in C:C[J]=A,B
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=A+O,B+P
						if 0<=D<K and 0<=E<L and g[D][E]!=8 and(D,E)not in F:F.add((D,E));I.append((D,E))
				if len(C)==2:
					N,Q=sorted(C);R,S=C[N];T=R+S&1
					for(A,B)in M:g[A][B]=N if A+B&1==T else Q
	return g