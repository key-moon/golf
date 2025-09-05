def	p(g):
	A=enumerate;E,F=len(g),len(g[0]);B=[[0]*F	for	_	in	range(E)];G={v	for	A	in	g	for	v	in	A	if	v}
	for	c	in	G:
		C=[i	for(i,A)in	A(g)for	v	in	A	if	v==c];D=[j	for(i,B)in	A(g)for(j,v)in	A(B)if	v==c];H,I=min(C),max(C)+1;J,K=min(D),max(D)+1
		for	i	in	range(H,I):
			for	j	in	range(J,K):B[i][j]=c
	return	B