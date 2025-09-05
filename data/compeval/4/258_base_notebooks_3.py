def	p(g):
	for	r	in	g:
		for	j	in	range(len(r)-2):
			if	r[j]&r[j+2]:r[j+1]=2
	return	g