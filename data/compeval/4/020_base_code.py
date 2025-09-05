def	p(g):
	G=len(g);A=[(i,j,g[i][j])for	i	in	range(G)for	j	in	range(G)if	g[i][j]];B=(min(i[0]for	i	in	A)+max(i[0]for	i	in	A))//2;C=(min(j[1]for	j	in	A)+max(j[1]for	j	in	A))//2
	for(D,E,F)in	A:g[B-(E-C)][C+(D-B)]=F;g[2*B-D][2*C-E]=F;g[B+(E-C)][C-(D-B)]=F
	return	g