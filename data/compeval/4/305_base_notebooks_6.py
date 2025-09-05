def	p(j):
	A=enumerate;c=len({c	for	A	in	j	for	c	in	A	if	c});B=[0]*c
	for(k,D)in	A(j):
		for(l,C)in	A(D):
			if	C:B[(k+l)%c]=C
	return[[B[(A+C)%c]for	C	in	range(len(j[0]))]for	A	in	range(len(j))]