def p(A):
	Q,N=len(A),len(A[0]);K=[[0]*N for A in A]
	for B in range(Q):
		for C in range(N):
			if A[B][C]and not K[B][C]:
				D=A[B][C];O=[(B,C)];K[B][C]=1;P=[]
				while O:
					L,M=O.pop();P.append((L,M))
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=L+T,M+U
						if 0<=E<Q and 0<=F<N and not K[E][F]and A[E][F]==D:K[E][F]=1;O.append((E,F))
				R=[A[0]for A in P];S=[A[1]for A in P];G,H,I,J=min(R),max(R),min(S),max(S)
				if H-G>1 and J-I>1 and all(A[G][B]==D for B in range(I,J+1))and all(A[H][B]==D for B in range(I,J+1))and all(A[B][I]==D for B in range(G,H+1))and all(A[B][J]==D for B in range(G,H+1)):
					for L in range(G+1,H):
						for M in range(I+1,J):A[L][M]=2
	return A