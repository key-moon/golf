from	collections	import*
def	p(g,k=range):
	X=[[8if	C==8else	0for	C	in	R]for	R	in	g]
	for	r	in	k(len(g)-1):
		for	c	in	k(len(g[0])-1):
			a=[g[r][c:c+2],g[r+1][c:c+2]];b=[x	for	R	in	a	for	x	in	R];C=Counter(b).most_common(1)
			if	C[0][1]==3and	C[0][0]!=0:
				for	i	in	k(r,r+2):
					for	j	in	k(c,c+2):
						if	X[i][j]==0:X[i][j]=1
	return	X