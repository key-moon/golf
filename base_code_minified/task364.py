def p(g):
	from collections import deque as O;L,D=len(g),len(g[0]);M=[[0]*D for A in g];E=[[0]*D for A in g]
	for F in range(L):
		for G in range(D):
			if g[F][G]==3 and not E[F][G]:
				J=O([(F,G)]);E[F][G]=1;A=[]
				while J:
					H,I=J.popleft();A.append((H,I))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=H+P,I+Q
						if 0<=B<L and 0<=C<D and g[B][C]==3 and not E[B][C]:E[B][C]=1;J.append((B,C))
				R=[A[0]for A in A];S=[A[1]for A in A];T,U=min(R),min(S);N=tuple(sorted((A-T)*100+(B-U)for(A,B)in A))
				if N[0]%2:K=1
				elif len(N)%3==2:K=6
				else:K=2
				for(H,I)in A:M[H][I]=K
	return M