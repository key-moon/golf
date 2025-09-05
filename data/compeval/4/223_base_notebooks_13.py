def	p(g):
	A=[]
	for	r	in	g:
		for	i	in	range(3):A+=[sum([[c]*3for	c	in	r],[])]
	return	A