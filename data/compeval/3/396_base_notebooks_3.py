def	p(g):
	A=range;h,w=len(g),len(g[0]);f={}
	for	i	in	A(h):
		for	j	in	A(w):
			if	g[i][j]:f[g[i][j]]=f.get(g[i][j],0)+1
	x,y=max(f,key=f.get),min(f,key=f.get);m,z=0,None
	for	t	in	A(h-2):
		for	l	in	A(w-2):
			for	b	in	A(t+2,h):
				for	r	in	A(l+2,w):
					if	all(g[t][j]==x	for	j	in	A(l,r+1))and	all(g[b][j]==x	for	j	in	A(l,r+1))and	all(g[i][l]==x	for	i	in	A(t,b+1))and	all(g[i][r]==x	for	i	in	A(t,b+1)):
						a=(b-t+1)*(r-l+1)
						if	a>m:m,z=a,(t,l,b,r)
	t,l,b,r=z;return[[y	if	g[t+i][l+j]==x	else	g[t+i][l+j]for	j	in	A(r-l+1)]for	i	in	A(b-t+1)]