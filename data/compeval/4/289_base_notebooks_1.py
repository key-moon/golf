import	numpy	as	np
def	p(g):A=[x	for	A	in	g	for	x	in	A];i=len(set(A))-1;return	np.kron(g,np.ones((i,i))).astype(int).tolist()