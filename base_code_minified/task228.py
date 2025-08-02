def p(A):
	F={}
	for(C,E)in enumerate(A):
		for(D,B)in enumerate(E):
			if B:F[B]=F.get(B,0)+1
	L=max(F,key=F.get);G=H=99;I=J=0
	for(C,E)in enumerate(A):
		for(D,B)in enumerate(E):
			if B==L:
				if C<G:G=C
				if C>I:I=C
				if D<H:H=D
				if D>J:J=D
	M=[]
	for(C,E)in enumerate(A):
		for(D,B)in enumerate(E):
			if B and B!=L:M+=C,D,B;A[C][D]=0
	K=iter(M)
	for(C,D,B)in zip(K,K,K):N=I+1 if C==G+1 else G-1;O=J+1 if D==H+1 else H-1;A[N][O]=B
	return A