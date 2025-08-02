def p(A):
	from collections import deque as E;N,F=len(A),len(A[0]);E=[[0]*F for A in A];G=[[0]*F for A in A]
	for H in range(N):
		for I in range(F):
			if A[H][I]==3 and not G[H][I]:
				L=E([(H,I)]);G[H][I]=1;B=[]
				while L:
					J,K=L.popleft();B.append((J,K))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=J+P,K+Q
						if 0<=C<N and 0<=D<F and A[C][D]==3 and not G[C][D]:G[C][D]=1;L.append((C,D))
				R=[A[0]for A in B];S=[A[1]for A in B];T,U=min(R),min(S);O=tuple(sorted((A-T)*100+(B-U)for(A,B)in B))
				if O[0]%2:M=1
				elif len(O)%3==2:M=6
				else:M=2
				for(J,K)in B:E[J][K]=M
	return E