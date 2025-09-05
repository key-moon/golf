def	p(g):
	A=len(g);C=max(max(A)for	A	in	g);B=[[0]*A*A	for	_	in	range(A*A)]
	for(D,E)in	enumerate(g):
		for(F,G)in	enumerate(E):
			if	G==C==2:
				for(H,I)in	enumerate(g):
					for(J,K)in	enumerate(I):B[D*A+H][F*A+J]=K
	return	B