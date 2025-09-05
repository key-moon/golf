def	p(g):
	B=[(A,C)for(A,B)in	enumerate(g)for(C,D)in	enumerate(B)if	D==8]
	for	C	in{A	for(A,_)in	B}:
		A=[B	for(A,B)in	B	if	A==C];a,b=min(A),max(A)
		for	D	in	range(a,b+1):g[C][D]=8
	for	D	in{A	for(_,A)in	B}:
		A=[A	for(A,B)in	B	if	B==D];a,b=min(A),max(A)
		for	C	in	range(a,b+1):g[C][D]=8
	return	g