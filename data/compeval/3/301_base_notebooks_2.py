from	collections	import*
def	p(j):
	A,c=len(j),len(j[0]);E=[W	for	s	in	j	for	W	in	s];k=Counter(E).most_common(10);k=[c	for	c	in	k	if	c[0]>0];j=[[0for	_	in	R]for	R	in	j]
	for	W	in	range(len(k)):j[-(W+1)]=j[-(W+1)][:c-k[W][1]]+[k[W][0]for	_	in	range(k[W][1])]
	return	j