def	p(j,A=range(4)):
	for	c	in	A:
		for	B	in	A:j[c][B]+=j[c+5][B]
	j=[[3if	c>0else	0for	c	in	c]for	c	in	j];return	j[:4]