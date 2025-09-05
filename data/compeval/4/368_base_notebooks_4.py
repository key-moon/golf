def	p(j,A=range):
	c=len(j);E=1;k,D=0,0;l=[0,5];F,a=0,0
	for	B	in	A(c):
		for	e	in	A(c):
			if	j[B][e]not	in	l	and	E:
				E=0;F,a=B,e;C=B;w=e
				while	C<c	and	j[C][e]not	in	l:C+=1
				while	w<c	and	j[B][w]not	in	l:w+=1
				k=C-B;D=w-e
	for	B	in	A(c-k+1):
		for	e	in	A(c-D+1):
			if	j[B][e]==5:
				for	G	in	A(k):
					for	b	in	A(D):j[B+G][e+b]=j[F+G][a+b]
	return	j