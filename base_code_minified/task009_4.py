def p(val_g):
	A=val_g;Q,N=len(A),len(A[0]);O=[A[0]for A in A if len(set(A))==1][0];K=[A for(A,B)in enumerate(A)if B.count(O)==N];G=[B for B in range(N)if all(A[C][B]==O for C in range(Q))];L,M=len(K)-1,len(G)-1
	def E(i,j):return[A[B][G[j]+1:G[j+1]]for B in range(K[i]+1,K[i+1])]
	F=lambda p:all(not B for A in p for B in A)
	def P(i,j,p):
		for(B,C)in enumerate(p):A[K[i]+1+B][G[j]+1:G[j+1]]=C
	for B in range(L):
		for C in range(M):
			D=E(B,C)
			if F(D):continue
			for H in range(C+1,M):
				I=E(B,H)
				if I==D:
					for J in range(C+1,H):
						if F(E(B,J)):P(B,J,D)
					break
				if not F(I):break
	for C in range(M):
		for B in range(L):
			D=E(B,C)
			if F(D):continue
			for H in range(B+1,L):
				I=E(H,C)
				if I==D:
					for J in range(B+1,H):
						if F(E(J,C)):P(J,C,D)
					break
				if not F(I):break
	return A