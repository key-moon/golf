def	p(g):
	h,w=len(g),len(g[0]);A=[[0]*(w*w)for	_	in	range(h*h)]
	for(B,C)in	enumerate(g):
		for(D,E)in	enumerate(C):
			if	E!=0:
				for(F,G)in	enumerate(g):
					for(H,I)in	enumerate(G):A[B*h+F][D*w+H]=I
	return	A