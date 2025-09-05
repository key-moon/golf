def	p(g,L=len,R=range):
	h,w,d=L(g),L(g[0]),{}
	for	r	in	R(h):
		for	c	in	R(w):
			A=g[r][c]
			if	A	in	d:d[A]['r']+=[r];d[A]['c']+=[c]
			else:d[A]={'r':[r],'c':[c]}
	B=sorted([[L(d[k]['r'])*(max(d[k]['c'])-min(d[k]['c'])),k]for	k	in	d	if	k>0])[0][1];g=[[B	if	A==B	else	0for	A	in	A]for	A	in	g];d=d[B];g=[A[min(d['c']):max(d['c'])+1]for	A	in	g];g=g[min(d['r']):max(d['r'])+1];return	g