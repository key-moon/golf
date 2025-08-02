def p(A):
	L,H=len(A),len(A[0]);E=[[0]*H for A in A];I=[]
	for F in range(L):
		for G in range(H):
			if A[F][G]==3 and not E[F][G]:
				B=[(F,G)];E[F][G]=1
				for(J,K)in B:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=J+M,K+N
						if 0<=C<L and 0<=D<H and A[C][D]==3 and not E[C][D]:E[C][D]=1;B.append((C,D))
				I.append(B)
	O=sorted({len(A)for A in I});P={A:B for(A,B)in zip(O,(1,2,6))}
	for B in I:
		for(J,K)in B:A[J][K]=P[len(B)]
	return A