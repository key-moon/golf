def p(A):
	H,I=len(A),len(A[0]);E=[(B,C)for B in range(H)for C in range(I)if 0<A[B][C]!=8];J=min(A for(A,B)in E);K=min(A for(B,A)in E);M={(B-J,C-K):A[B][C]for(B,C)in E};L=[]
	for B in range(H):
		for C in range(I):
			if A[B][C]==8:
				D=[(B,C)];A[B][C]=0
				for N in range(len(D)):
					O,P=D[N]
					for(Q,R)in((1,0),(-1,0),(0,1),(0,-1)):
						F,G=O+Q,P+R
						if 0<=F<H and 0<=G<I and A[F][G]==8:A[F][G]=0;D.append((F,G))
				L.append((min(A for(A,B)in D),min(A for(B,A)in D)))
	for(B,C)in E:A[B][C]=0
	for(J,K)in L:
		for((S,T),U)in M.items():A[J+S][K+T]=U
	return A