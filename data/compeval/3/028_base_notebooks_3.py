def	p(g):
	q=range;r=[[0]*10for	_	in	q(10)]
	for	i	in	q(5):
		for	j	in	q(10):
			if	g[i][j]:
				v=g[i][j];r[0]=[v]*10;r[i]=[v]*10
				for	k	in	q(5):
					if	k	not	in[0,i]:r[k][0]=r[k][9]=v
	for	i	in	q(5,10):
		for	j	in	q(10):
			if	g[i][j]:
				v=g[i][j];r[i]=[v]*10;r[9]=[v]*10
				for	k	in	q(5,10):
					if	k	not	in[i,9]:r[k][0]=r[k][9]=v
	return	r