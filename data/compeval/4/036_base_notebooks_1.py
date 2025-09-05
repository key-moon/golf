def	p(j,A=len,c=range):
	C='r';k='c';F,l,B=A(j),A(j[0]),{}
	for	a	in	c(F):
		for	D	in	c(l):
			e=j[a][D]
			if	e	in	B:B[e][C]+=[a];B[e][k]+=[D]
			else:B[e]={C:[a],k:[D]}
	E=sorted([[A(B[e][C])*(max(B[e][k])-min(B[e][k])),e]for	e	in	B	if	e>0])[0][1];j=[[E	if	A==E	else	0for	A	in	A]for	A	in	j];B=B[E];j=[A[min(B[k]):max(B[k])+1]for	A	in	j];j=j[min(B[C]):max(B[C])+1];return	j