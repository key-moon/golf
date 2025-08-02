def p(A):
	M,K=len(A),len(A[0]);G=[[0]*K for A in A];N={}
	for H in range(M):
		for I in range(K):
			if A[H][I]and not G[H][I]:
				L=[(H,I)];G[H][I]=1;B=[]
				while L:
					O,P=L.pop();B.append((O,P))
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=O+U,P+V
						if 0<=E<M and 0<=F<K and A[E][F]and not G[E][F]:G[E][F]=1;L.append((E,F))
				C=min(A for(A,B)in B);D=min(A for(B,A)in B);Q=tuple(sorted((A-C,B-D)for(A,B)in B));N.setdefault(Q,[]).append((C,D,B))
	for(Q,R)in N.items():
		for(C,D,B)in R:
			if len({A[B][C]for(B,C)in B})>1:J=C,D,B;break
		W={(B-J[0],C-J[1]):A[B][C]for(B,C)in J[2]}
		for(C,D,B)in R:
			if B!=J[2]:
				for(S,T)in B:A[S][T]=W[S-C,T-D]
	return A