def p(g):
	D=[A[:]for A in g];E,F=len(g),len(g[0]);B,C,A=E-1,0,1
	while B>=0:
		D[B][C]=1
		if 0<=C+A<F:B-=1;C+=A
		else:B-=1;A=-A;C+=A
	return D