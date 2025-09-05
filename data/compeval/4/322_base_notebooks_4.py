def	p(m,y=range):
	for	c	in	y(len(m[0])):
		for	r	in	y(len(m)):
			if	m[r][c]:break
		else:continue
		for	i	in	y(r,len(m)):m[i][c]=m[r][c]
	return	m