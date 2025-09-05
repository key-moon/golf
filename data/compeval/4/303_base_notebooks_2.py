def	p(j,A=range):
	c,B=len(j),len(j[0])
	for	k	in	A(c):
		if	sum(j[k])==0:j[k]=[2]*B
	for	C	in	A(B):
		if	all(j[k][C]in[0,2]for	k	in	A(c)):
			for	k	in	A(c):j[k][C]=2
	return	j