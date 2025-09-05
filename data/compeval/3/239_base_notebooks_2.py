from	collections	import*
def	p(g):
	C=Counter([x	for	r	in	g	for	x	in	r]).most_common(9);h,w=C[0][1],len(C);g=[[0for	_	in	range(w)]for	_	in	range(h)]
	for	i	in	range(w):
		for	j	in	range(C[i][1]):g[j][i]=C[i][0]
	return	g