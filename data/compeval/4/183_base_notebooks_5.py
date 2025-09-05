def	p(g):
	A=range;n=len(g);s=n//2-2;r=[];c=[g[0][0],g[0][-1],g[-1][0],g[-1][-1]]
	for	i	in	A(2,n-2):
		t=[]
		for	j	in	A(2,n-2):
			v=g[i][j]
			if	v==8:x=(i-2)//s;y=(j-2)//s;v=c[x*2+y]
			t.append(v)
		r.append(t)
	return	r