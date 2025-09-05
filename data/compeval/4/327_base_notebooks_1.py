def	p(g):
	B=[];C=enumerate;D=[[0,0,0,0,0,0]for	_	in	range(6)]
	for(r,E)in	C(g):
		for(c,F)in	C(E):
			if	g[r][c]>0:B.append([r,c])
		for	A	in	B:
			for	i	in	range(10):
				try:D[A[0]+i][A[1]+i]=g[A[0]][A[1]]
				except:pass
	return	D