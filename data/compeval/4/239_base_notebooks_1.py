from	collections	import*
def	p(g,F=range):
	C=Counter([x	for	r	in	g	for	x	in	r]).most_common(9);h,w=C[0][1],len(C);g=[[0for	_	in	F(w)]for	_	in	F(h)]
	for	i	in	F(w):
		for	j	in	F(C[i][1]):g[j][i]=C[i][0]
	return	g