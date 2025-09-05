from	collections	import*
def	p(g,u=range):
	C=Counter([x	for	r	in	g	for	x	in	r]).most_common(9);h,w=C[0][1],len(C);g=[[0for	_	in	u(w)]for	_	in	u(h)]
	for	i	in	u(w):
		for	j	in	u(C[i][1]):g[j][i]=C[i][0]
	return	g