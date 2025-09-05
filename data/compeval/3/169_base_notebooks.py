def	p(j):
	F=range;c=[A[:]for	A	in	j];D=set();k=[(0,1),(1,0),(0,-1),(-1,0)]
	for	B	in	F(10):
		for	l	in	F(10):
			if	j[B][l]==5and(B,l)not	in	D:
				C,a=set(),[(B,l)];C.add((B,l));D.add((B,l))
				while	a:
					E,e=a.pop(0)
					for(G,w)in	k:
						A,b=E+G,e+w
						if	0<=A<10and	0<=b<10and	j[A][b]==5and(A,b)not	in	C:C.add((A,b));D.add((A,b));a.append((A,b))
				d=5-len(C)
				for(E,e)in	C:c[E][e]=d
	return	c