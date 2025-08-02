def p(A):
	G=next(A for B in A for A in B if A);H,I=len(A),len(A[0]);K=[(B,C)for B in range(H)for C in range(I)if A[B][C]==G];K.sort();E,F=K[0]
	if K[1][0]==E:C=[(0,1),(1,0)]
	else:C=[(1,0),(0,1)]
	B=1
	while 0<=E+C[0][0]*B<H and 0<=F+C[0][1]*B<I and A[E+C[0][0]*B][F+C[0][1]*B]==G:B+=1
	L=B;E+=C[0][0]*(B-1);F+=C[0][1]*(B-1);B=1
	while 0<=E+C[1][0]*B<H and 0<=F+C[1][1]*B<I and A[E+C[1][0]*B][F+C[1][1]*B]==G:B+=1
	M=B;D=[E,F];J=0
	while 1:
		for N in range(L if J%2==0 else M):
			D[0]+=C[J%2][0];D[1]+=C[J%2][1]
			if D[0]<0 or D[0]>=H or D[1]<0 or D[1]>=I:return A
			A[D[0]][D[1]]=G
		J+=1