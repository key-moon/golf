def p(A):
	R=len(A);O=len(A[0]);I={}
	for U in A:
		for S in U:I[S]=I.get(S,0)+1
	T=max(I,key=I.get);J=[[0]*O for A in A];V=[(1,0),(-1,0),(0,1),(0,-1)];P=[]
	for K in range(R):
		for L in range(O):
			if A[K][L]!=T and not J[K][L]:
				B=[(K,L)];J[K][L]=1
				for(W,X)in B:
					for(C,D)in V:
						E,F=W+C,X+D
						if 0<=E<R and 0<=F<O and A[E][F]!=T and not J[E][F]:J[E][F]=1;B.append((E,F))
				M,N=zip(*B);G,H,b,c=min(M),max(M),min(N),max(N);C=max(M)-min(M)+1;D=max(N)-min(N)+1;P.append((G,H,C,D,B))
	for(G,H,C,D,B)in P:
		if len(B)!=C*D or len({A[B][C]for(B,C)in B})>1:Q=C,D,[(B-G,C-H,A[B][C])for(B,C)in B];break
	for(G,H,C,D,B)in P:
		if(C,D)==(Q[0],Q[1])and len(B)==C*D:
			for(Y,Z,a)in Q[2]:A[G+Y][H+Z]=a
	return A