def	p(j,A=range(4)):
	for	c	in	A:
		for	B	in	A:
			j[c][B]+=j[c+5][B]
			if	j[c][B]==3:j[c][B]=0
			elif	j[c][B]>0:j[c][B]=3
	return	j[:4]