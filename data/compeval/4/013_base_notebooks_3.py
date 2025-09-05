def	p(g,z=range):
	r,c=len(g),len(g[0]);p=[(i,j,g[i][j])for	i	in	z(r)for	j	in	z(c)if	g[i][j]];p.sort()
	if	len(p)==2:
		a,b=p
		if	a[0]==b[0]:
			i,n,A=a;C,B=b[1],b[2];d=abs(C-n)
			for	x	in	z(r):g[x][n]=A;g[x][C]=B
			if	d:
				j=max(n,C)+d;k=0;v=[A,B]
				if	C<n:v=v[::-1]
				while	j<c:
					for	x	in	z(r):g[x][j]=v[k%2]
					j+=d;k+=1
		elif	a[1]==b[1]:
			j,E,A=a[1],a[0],a[2];D,B=b[0],b[2];d=abs(D-E)
			for	x	in	z(c):g[E][x]=A;g[D][x]=B
			if	d:
				i=D+d;k=0;v=[A,B]
				while	i<r:
					for	x	in	z(c):g[i][x]=v[k%2]
					i+=d;k+=1
		elif	a[0]==0and	b[0]==r-1:
			E,n,A=a;D,C,B=b;d=abs(C-n)
			for	x	in	z(r):g[x][n]=A;g[x][C]=B
			if	d:
				j=C+d;k=0;v=[A,B]
				while	j<c:
					for	x	in	z(r):g[x][j]=v[k%2]
					j+=d;k+=1
		elif	a[1]==0and	b[1]==c-1or	b[1]==0and	a[1]==c-1:
			if	a[1]==0:E,n,A=a;D,C,B=b
			else:E,n,A=b;D,C,B=a
			d=abs(D-E)
			for	x	in	z(c):g[E][x]=A;g[D][x]=B
			if	d:
				i=max(E,D)+d;k=0;v=[A,B]
				if	D<E:v=v[::-1]
				while	i<r:
					for	x	in	z(c):g[i][x]=v[k%2]
					i+=d;k+=1
	return	g