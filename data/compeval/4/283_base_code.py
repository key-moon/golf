def	p(g):
	for	A	in	range(len(g)):
		for	B	in	range(len(g[0])):
			if	g[A][B]==5:
				C=A
				while	C+1<len(g)and	g[C+1][B]==5:C+=1
				D=B
				while	D+1<len(g[0])and	g[A][D+1]==5:D+=1
				for	E	in	range(A,C+1):
					for	F	in	range(B,D+1):
						if	g[E][F]==5:g[E][F]=1if	E	in(A,C)and	F	in(B,D)else	4if	E	in(A,C)or	F	in(B,D)else	2
	return	g