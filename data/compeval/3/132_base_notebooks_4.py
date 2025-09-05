def	p(g,F=range):
	A=enumerate;C,D=len(g),len(g[0]);a=[[0]*D	for	_	in	F(C)];E={v	for	s	in	g	for	v	in	s	if	v}
	for	c	in	E:
		m=[i	for(i,s)in	A(g)for	v	in	s	if	v==c];B=[j	for(i,s)in	A(g)for(j,v)in	A(s)if	v==c];G,o=min(m),max(m)+1;H,I=min(B),max(B)+1
		for	i	in	F(G,o):
			for	j	in	F(H,I):a[i][j]=c
	return	a