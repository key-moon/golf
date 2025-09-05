def	p(g):
	A=[];B=enumerate;C=[[0,0,0,0,0,0]for	_	in	range(6)]
	for(r,D)in	B(g):
		for(c,E)in	B(D):
			if	g[r][c]>0:A.append([r,c])
		for	k	in	A:
			for	i	in	range(10):
				try:C[k[0]+i][k[1]+i]=g[k[0]][k[1]]
				except:pass
	return	C