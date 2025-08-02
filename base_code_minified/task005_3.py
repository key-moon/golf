def p(g):
	import collections,sys;R=len(g);P=len(g[0]);I=[[False]*P for A in g];Q=[]
	for E in range(R):
		for F in range(P):
			if g[E][F]and not I[E][F]:
				S=g[E][F];T=[(E,F)];I[E][F]=1;U=[]
				for(V,W)in T:
					U.append((V,W))
					for(G,H)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=V+G,W+H
						if 0<=A<R and 0<=B<P and not I[A][B]and g[A][B]==S:I[A][B]=1;T.append((A,B))
				Q.append((S,U))
	for(Z,(a,C))in enumerate(Q):
		for(b,(c,D))in enumerate(Q):
			if Z>=b or a==c:continue
			X=[A for(A,B)in C];Y=[A for(A,B)in D]
			if max(X)<min(Y)or max(Y)<min(X):continue
			J=min(A for(A,B)in C);K=min(A for(B,A)in C);L=min(A for(A,B)in D);M=min(A for(B,A)in D);d=max(A for(A,B)in D)-L+1;e=max(A for(B,A)in D)-M+1;f=max(A for(A,B)in C)-J+1;h=max(A for(B,A)in C)-K+1
			for(N,O)in C:
				G=N-J;H=O-K
				for(A,B)in D:g[L+(A-L)+G*d][M+(B-M)+H*e]=g[A][B]
			for(A,B)in D:
				G=A-L;H=B-M
				for(N,O)in C:g[J+(N-J)+G*f][K+(O-K)+H*h]=g[N][O]
	return g