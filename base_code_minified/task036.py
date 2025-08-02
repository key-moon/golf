def p(g):
	I,J=len(g),len(g[0]);F=set();A=set();K=0
	for B in range(I):
		for C in range(J):
			if g[B][C]and(B,C)not in F:
				L=g[B][C];G=[(B,C)];F.add((B,C));H={(B,C)}
				while G:
					M,N=G.pop()
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=M+O,N+P
						if 0<=D<I and 0<=E<J and g[D][E]==L and(D,E)not in F:F.add((D,E));G.append((D,E));H.add((D,E))
				if len(H)>len(A):A=H;K=L
	Q,R=min(A for(A,B)in A),max(A for(A,B)in A);S,T=min(A for(B,A)in A),max(A for(B,A)in A);return[[K if(B,C)in A else 0 for C in range(S,T+1)]for B in range(Q,R+1)]