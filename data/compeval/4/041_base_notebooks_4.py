def	p(g):
	z=0;A=False;B=enumerate
	for(r,D)in	B(g):
		for(c,C)in	B(D):
			if	C!=0:
				if	A==False:A=True;z=int(C)
				else:A=False;z=0
			else:g[r][c]=z
	return	g