def p(g):
	E={}
	for(B,D)in enumerate(g):
		for(C,A)in enumerate(D):
			if A:E[A]=E.get(A,0)+1
	K=max(E,key=E.get);F=G=99;H=I=0
	for(B,D)in enumerate(g):
		for(C,A)in enumerate(D):
			if A==K:
				if B<F:F=B
				if B>H:H=B
				if C<G:G=C
				if C>I:I=C
	L=[]
	for(B,D)in enumerate(g):
		for(C,A)in enumerate(D):
			if A and A!=K:L+=B,C,A;g[B][C]=0
	J=iter(L)
	for(B,C,A)in zip(J,J,J):M=H+1 if B==F+1 else F-1;N=I+1 if C==G+1 else G-1;g[M][N]=A
	return g