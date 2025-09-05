def	p(g):
	A=[]
	for	i	in	range(3):
		B=list(set(g[i]))
		if	len(B)>1:A.append([0]*3)
		else:A.append([5]*3)
	return	A