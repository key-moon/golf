def	p(g,E=enumerate):
	A=[]
	for(r,C)in	E(g):
		for(c,B)in	E(C):
			if	B	not	in[0,8]:A+=[[r,c,B]];g[r][c]=0
	D=A[0][:];A=[[x[0]-D[0],x[1]-D[1],x[2]]for	x	in	A]
	for(r,C)in	E(g):
		for(c,B)in	E(C):
			if	B==8:
				g[r][c]=D[2]
				for	x	in	A:g[r+x[0]][c+x[1]]=x[2]
	return	g