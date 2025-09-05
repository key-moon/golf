def	p(j):
	A,c=len(j),len(j[0]);B=j[0]*20
	for	k	in	range(2,A):j[k]=[B[k-2]for	_	in	range(c)]
	return	j