def	p(g):
	r,c=len(g),len(g[0]);s={(i,j)for	i	in	range(r)for	j	in	range(c)if	g[i][j]==2};t=s;o={(i,j)for	i	in	range(r)for	j	in	range(c)if	g[i][j]==8};A,B=zip(*s);E,F=min(A),max(A);G,H=min(B),max(B);A,B=zip(*o);I,J=min(A),max(A);K,L=min(B),max(B);C=I+J-E-F;D=K+L-G-H
	if	abs(C)>abs(D):D=0;C=C>0and	1or-1
	else:C=0;D=D>0and	1or-1
	while	1:
		u={(i+C,j+D)for(i,j)in	s}
		if	any(i<0	or	i>=r	or	j<0	or	j>=c	or(i,j)in	o	for(i,j)in	u):break
		s=u
	for(i,j)in	t:g[i][j]=0
	for(i,j)in	s:g[i][j]=2
	return	g