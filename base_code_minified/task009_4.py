def p(A):
	O,L=len(A),len(A[0]);M=[A[0]for A in A if len(set(A))==1][0];P=[A for(A,B)in enumerate(A)if B.count(M)==L];Q=[B for B in range(L)if all(A[C][B]==M for C in range(O))];J,K=len(P)-1,len(Q)-1
	def E(A,B):return[val_g[A][val_c[B]+1:val_c[B+1]]for A in range(val_r[A]+1,val_r[A+1])]
	F=lambda P:all(not B for A in P for B in A)
	def N(A,B,C):
		for(D,E)in enumerate(C):val_g[val_r[A]+1+D][val_c[B]+1:val_c[B+1]]=E
	for B in range(J):
		for C in range(K):
			D=E(B,C)
			if F(D):continue
			for G in range(C+1,K):
				H=E(B,G)
				if H==D:
					for I in range(C+1,G):
						if F(E(B,I)):N(B,I,D)
					break
				if not F(H):break
	for C in range(K):
		for B in range(J):
			D=E(B,C)
			if F(D):continue
			for G in range(B+1,J):
				H=E(G,C)
				if H==D:
					for I in range(B+1,G):
						if F(E(I,C)):N(I,C,D)
					break
				if not F(H):break
	return A