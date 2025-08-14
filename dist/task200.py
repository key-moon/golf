A=range
def	p(g):
	C=next(filter(None,g[-1]));D=g[-1].index(C)
	for	B	in	A(D,10,2):
		for	E	in	A(10):g[E][B]=C
	for(F,B)in	enumerate(A(D+1,10,2)):g[(F&1)*9][B]=5
	return	g