def p(g):
	C,D=len(g),len(g[0]);E=[(A,B)for A in range(C)for B in range(D)if(A<1 or A>C-2 or B<1 or B>D-2)and not g[A][B]]
	while E:
		A,B=E.pop()
		if 0<=A<C and 0<=B<D and not g[A][B]:g[A][B]=-1;E+=[(A+1,B),(A-1,B),(A,B+1),(A,B-1)]
	for A in range(C):
		for B in range(D):
			if g[A][B]<0:g[A][B]=0
			elif not g[A][B]:g[A][B]=1
	return g