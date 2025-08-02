def p(A):
	C=len(A);K=[]
	for F in range(C):
		for G in range(C):
			if A[F][G]==5:
				B=[(F,G)];A[F][G]=0;H=0
				while H<len(B):
					I,J=B[H];H+=1
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=I+L,J+M
						if 0<=D<C and 0<=E<C and A[D][E]==5:A[D][E]=0;B+=[(D,E)]
				K+=[B]
	for(N,B)in enumerate(sorted(K,key=len)):
		for(I,J)in B:A[I][J]=[2,4,1][N]
	return A