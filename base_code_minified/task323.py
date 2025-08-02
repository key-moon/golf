def p(g):
	F=len(g)
	for(D,A)in enumerate(g):
		if 8 in A:I=A.index(8);break
	for(E,A)in enumerate(g):
		if E==D:continue
		G=abs(D-E);H=1 if E<D else-1;B=I+H*G
		if G&1:
			C=B-H
			if 0<=C<F:A[C]=5
		else:
			for C in range(B-2,B+1)if E<D else range(B,B+3):
				if 0<=C<F:A[C]=5
	return g