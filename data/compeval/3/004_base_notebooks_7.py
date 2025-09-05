def	p(g):
	s={}
	for(r,C)in	enumerate(g):
		for(c,A)in	enumerate(C):
			if	A:s.setdefault(A,[]).append((r,c))
	o=[[0]*len(g[0])for	_	in	g]
	for(A,B)in	s.items():
		D,E=max(r	for(r,_)in	B),max(c	for(_,c)in	B)
		for(r,c)in	B:o[r][c	if	r==D	or	c==E	else	c+1]=A
	return	o