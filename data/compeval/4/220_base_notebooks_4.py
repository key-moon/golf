def	p(j,A=enumerate):
	c={8:4,2:1,3:6};B=[[A	for(a,A)in	A(B)]for	B	in	j]
	for(k,E)in	A(j):
		for(l,C)in	A(E):
			if	C:
				for	a	in	range(-1,2):
					for	D	in	range(-1,2):
						try:
							if[a,D]!=[0,0]:B[k+a][l+D]=c[C]
						except:0
	return	B