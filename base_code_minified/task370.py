def p(A):
	G=A[0][0];H,I=len(A),len(A[0])
	for B in range(H):
		for C in range(I):
			D=A[B][C]
			if D-G and D:J,K,L=B,C,D;break
		else:continue
		break
	for(E,F)in((1,1),(1,-1),(-1,1),(-1,-1)):
		B,C=J,K
		while 0<=B+E<H and 0<=C+F<I and A[B+E][C+F]==G:B+=E;C+=F;A[B][C]=L
	return A