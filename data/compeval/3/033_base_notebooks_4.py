def	p(j):
	A=range;c=[A[:]for	A	in	j];E=j[5][0];k=[[j[l+1][A+1]for	A	in	A(3)]for	l	in	A(3)]
	for	D	in[(0,6),(0,12),(6,0),(6,6),(6,12),(12,0),(12,6),(12,12)]:
		for	l	in	A(3):
			for	B	in	A(3):a,C=D[0]+l+1,D[1]+B+1;c[a][C]=j[a][C]if	k[l][B]==j[a][C]else	E	if	k[l][B]else	0
	return	c