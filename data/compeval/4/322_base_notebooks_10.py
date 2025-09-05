def	p(m,B=range):
	for	c	in	B(len(m[0])):
		for	r	in	B(len(m)):
			if	m[r][c]:break
		else:continue
		for	i	in	B(r,len(m)):m[i][c]=m[r][c]
	return	m