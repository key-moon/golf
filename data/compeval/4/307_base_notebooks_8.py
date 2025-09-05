def	p(g):
	A=[]
	for	r	in	g:
		for	i	in	range(2):A+=[sum([[c]*2for	c	in	r],[])]
	return	A