def	p(g):
	C=[r[:2]for	r	in	g[:2]];h,w=2,2;A=[]
	for	i	in	range(h):
		B=[]
		for	j	in	range(w):B.append(C[i%2][j%2])
		A.append(B)
	return	A