D=range
def	p(g):
	for	A	in	D(len(g[0])):
		if	g[-1][A]==2:
			B=0
			for	C	in	D(len(g)):
				if	g[-(C+1)][A+B]==5:B+=1;g[-C][A+B]=2
				g[-(C+1)][A+B]=2
	return	g