def	p(m):
	r,c=len(m),len(m[0]);o=[r[:]for	r	in	m];i,j=next((i,j)for	i	in	range(r)for	j	in	range(c)if	m[i][j])
	for(A,b)in(-1,1),(1,-1):
		x,y=i,j
		while	1:
			for	_	in[0]*2:
				x+=A
				if	0<=x<r:o[x][y]=5
				else:break
			else:
				for	_	in[0]*2:
					y+=b
					if	0<=y<c:o[x][y]=5
					else:break
				else:continue
			break
	return	o