def	p(j):
	j=[j[0]]+j+[j[-1]];j=[[A[0]]+A+[A[-1]]for	A	in	j]
	for(A,c)in[[0,0],[0,-1],[-1,0],[-1,-1]]:j[A][c]=0
	return	j