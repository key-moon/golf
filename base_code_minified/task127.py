def p(A):
	B,C=len(A),len(A[0]);J=[B for B in range(B)if A[B]==[5]*C];D=J and[0]+J+[B]or[0,B];M=[C for C in range(C)if all(A[B][C]==5 for B in range(B))];E=[0]+M+[C]
	for F in range(len(D)-1):
		for G in range(len(E)-1):
			H=D[F]+(F>0);K=D[F+1];I=E[G]+(G>0);L=E[G+1];N=A[H+(K-H)//2][I+(L-I)//2]+5
			for O in range(H,K):
				for P in range(I,L):A[O][P]=N
	return A