def p(A):
	E,F=len(A),len(A[0]);D=[(B,C)for B in range(E)for C in range(F)if A[B][C]==0]
	for(B,C)in D:
		if(B-1,C)in D and(B+1,C)in D and(B,C-1)in D and(B,C+1)in D:H,I=B,C;break
	L=A[0][0]
	for B in range(E):
		for C in range(F):
			if A[B][C]!=L and A[B][C]!=0:M,N,O=B,C,A[B][C];break
		else:continue
		break
	P,Q=M-H,N-I;G=1
	while 1:
		J,K=H+P*G,I+Q*G
		if not(0<=J<E and 0<=K<F):break
		A[J][K]=O;G+=1
	return A