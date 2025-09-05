def	p(g):
	A=range;n,m=len(g),len(g[0]);r=[i	for	i	in	A(n)if	all(g[i][j]==0for	j	in	A(m))];c=[j	for	j	in	A(m)if	all(g[i][j]==0for	i	in	A(n))];r=[-1]+r+[n];c=[-1]+c+[m];o=[]
	for	i	in	A(len(r)-1):
		t=[]
		for	j	in	A(len(c)-1):
			for	x	in	A(r[i]+1,r[i+1]):
				for	y	in	A(c[j]+1,c[j+1]):
					if	g[x][y]:t.append(g[x][y]);break
				else:continue
				break
		if	t:o.append(t)
	return	o