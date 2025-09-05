def	p(g):
	A=enumerate
	for(r,E)in	A(g):
		i,B,C=0,[],False
		for(c,D)in	A(E):
			if	D>0:B=[D,5]*20;C=True
			if	C:g[r][c]=B[i];i+=1
	return	g