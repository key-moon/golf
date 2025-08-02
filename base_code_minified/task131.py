def p(A):
	try:B=next(B for(B,A)in enumerate(A)if A.count(2)==len(A));K='r'
	except:B=next(B for B in range(len(A[0]))if all(A[B]==2 for A in A));K='c'
	C=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==3];G=min(A for(A,B)in C);L=max(A for(A,B)in C);H=min(A for(B,A)in C);M=max(A for(B,A)in C);I=L-G+1;J=M-H+1
	if K=='c':
		if M<B:N=B-J-H;F=B-J-1
		else:N=B+1-H;F=B+1+J
		for(D,E)in C:A[D][E]=0;A[D][E+N]=3;A[D][F]=8
	else:
		if L<B:O=B-I-G;F=B-I-1
		else:O=B+1-G;F=B+1+I
		for(D,E)in C:A[D][E]=0;A[D+O][E]=3;A[F][E]=8
	return A