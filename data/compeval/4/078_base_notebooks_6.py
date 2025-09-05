def	p(g):
	d={i:0for	i	in	range(len(g[0]))};B=[[1if	A==1else	0for	A	in	A]for	A	in	g];A=enumerate
	for(r,C)in	A(g):
		for(c,D)in	A(C):
			if	D==2:d[c]+=1
	for(r,C)in	A(B):
		for(c,D)in	A(C):
			if	D==0and	d[c]>0:B[r][c]=2;d[c]-=1
	return	B