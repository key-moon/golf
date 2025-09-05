def	p(g):
	B=enumerate;A=len({A	for	B	in	g	for	A	in	B	if	A});C=[0]*A
	for(E,F)in	B(g):
		for(G,D)in	B(F):
			if	D:C[(E+G)%A]=D
	return[[C[(B+D)%A]for	D	in	range(len(g[0]))]for	B	in	range(len(g))]