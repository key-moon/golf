def p(j):
	D=[A[:]for A in j];E,F=len(j),len(j[0]);B,C,A=E-1,0,1
	while B>=0:
		D[B][C]=1
		if 0<=C+A<F:B-=1;C+=A
		else:B-=1;A=-A;C+=A
	return D