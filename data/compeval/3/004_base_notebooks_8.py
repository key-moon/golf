def	p(g):
	s={};C=enumerate
	for(r,D)in	C(g):
		for(c,A)in	C(D):
			if	A:s.setdefault(A,[]).append((r,c))
	o=[[0]*len(g[0])for	_	in	g]
	for(A,B)in	s.items():
		E,F=max(r	for(r,_)in	B),max(c	for(_,c)in	B)
		for(r,c)in	B:o[r][c	if	r==E	or	c==F	else	c+1]=A
	return	o