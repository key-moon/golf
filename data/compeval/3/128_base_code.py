def	p(g):
	E,F=len(g),len(g[0]);A=[E]*5;B=[-1]*5
	for(y,C)in	enumerate(g):
		for(x,v)in	enumerate(C):
			if	v:
				if	y<A[v]:A[v]=y
				if	y>B[v]:B[v]=y
	D=[[0]*F	for	_	in	g]
	for(y,C)in	enumerate(g):
		for(x,v)in	enumerate(C):
			if	v:D[y-(B[v]-A[v]+1)][x]=v
	return	D