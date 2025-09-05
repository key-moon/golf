def	p(j,A=enumerate):
	for(c,B)in	A(j):
		for(k,C)in	A(B):
			if	c<len(j)//2:j[c][k]=j[-(c+1)][k]
	return	j