def p(g):
	K=len(g);I=len(g[0]);F=[[0]*I for A in g];G={}
	for A in range(K):
		for B in range(I):
			if g[A][B]and not F[A][B]:
				C=g[A][B];J=[(A,B)];F[A][B]=1;H=[]
				while J:
					L,M=J.pop();H.append((L,M))
					for(O,P)in((1,0),(0,1),(-1,0),(0,-1)):
						D,E=L+O,M+P
						if 0<=D<K and 0<=E<I and not F[D][E]and g[D][E]==C:F[D][E]=1;J.append((D,E))
				Q=min(A for(A,B)in H);R=min(A for(B,A)in H);S=tuple(C if(Q+A,R+B)in H else 0 for A in range(3)for B in range(3));G.setdefault(C,[]).append(S)
	C=max(G,key=lambda k:len(G[k]));N=G[C];T=max(set(N),key=N.count);return[list(T[A*3:(A+1)*3])for A in range(3)]