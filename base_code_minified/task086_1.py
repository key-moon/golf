def p(A):
	R,S=len(A),len(A[0]);J=[A[:]for A in A];H=set()
	for D in range(R):
		for E in range(S):
			if A[D][E]and(D,E)not in H:
				K=A[D][E];I=[(D,E)];H.add((D,E))
				for T in I:
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=T[0]+U,T[1]+V
						if 0<=B<R and 0<=C<S and A[B][C]==K and(B,C)not in H:H.add((B,C));I.append((B,C))
				F=[A[0]for A in I];G=[A[1]for A in I];L,M=min(F)-1,max(F)+1;N,O=min(G)-1,max(G)+1;P=[]
				for B in range(L+1,M):
					for C in range(N+1,O):
						Q=A[B][C]
						if Q and Q!=K:P.append((B,C));W=Q
				F=[A[0]for A in P];G=[A[1]for A in P];X,Y=min(F)-1,max(F)+1;Z,a=min(G)-1,max(G)+1
				for B in range(L,M+1):
					for C in range(N,O+1):
						if B in(L,M)or C in(N,O):J[B][C]=K
				for B in range(X,Y+1):
					for C in range(Z,a+1):J[B][C]=W
	return J