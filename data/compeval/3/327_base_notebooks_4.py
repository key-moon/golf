def	p(g):
	A=[];B=enumerate;C=[[0,0,0,0,0,0]for	_	in	range(6)]
	for(r,D)in	B(g):
		for(c,E)in	B(D):
			if	g[r][c]>0:A.append([r,c])
		for	j	in	A:
			for	i	in	range(10):
				try:C[j[0]+i][j[1]+i]=g[j[0]][j[1]]
				except:pass
	return	C