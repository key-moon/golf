def	p(g):
	C=[r[:2]for	r	in	g[:2]];A=[]
	for	i	in	range(2):
		B=[]
		for	j	in	range(2):B.append(C[i%2][j%2])
		A.append(B)
	return	A