def p(A):
	import collections,sys;S=len(A);Q=len(A[0]);J=[[False]*Q for A in A];R=[]
	for F in range(S):
		for G in range(Q):
			if A[F][G]and not J[F][G]:
				T=A[F][G];U=[(F,G)];J[F][G]=1;V=[]
				for(W,X)in U:
					V.append((W,X))
					for(H,I)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=W+H,X+I
						if 0<=B<S and 0<=C<Q and not J[B][C]and A[B][C]==T:J[B][C]=1;U.append((B,C))
				R.append((T,V))
	for(a,(b,D))in enumerate(R):
		for(c,(d,E))in enumerate(R):
			if a>=c or b==d:continue
			Y=[A for(A,B)in D];Z=[A for(A,B)in E]
			if max(Y)<min(Z)or max(Z)<min(Y):continue
			K=min(A for(A,B)in D);L=min(A for(B,A)in D);M=min(A for(A,B)in E);N=min(A for(B,A)in E);e=max(A for(A,B)in E)-M+1;f=max(A for(B,A)in E)-N+1;g=max(A for(A,B)in D)-K+1;h=max(A for(B,A)in D)-L+1
			for(O,P)in D:
				H=O-K;I=P-L
				for(B,C)in E:A[M+(B-M)+H*e][N+(C-N)+I*f]=A[B][C]
			for(B,C)in E:
				H=B-M;I=C-N
				for(O,P)in D:A[K+(O-K)+H*g][L+(P-L)+I*h]=A[O][P]
	return A