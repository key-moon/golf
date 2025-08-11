def p(g):
	F=range;D=len(g);H=[[0]*D for A in F(D)];B,A=0,0;G=[(0,1),(1,0),(0,-1),(-1,0)]
	for I in F(D):
		H[B][A]=3
		if I<D-1:A+=1
	E=D-1;C=1
	while E>0:
		for J in F(2):
			if E>0:
				B,A=B+G[C][0],A+G[C][1]
				for I in F(E):
					H[B][A]=3
					if I<E-1:B,A=B+G[C][0],A+G[C][1]
				C=(C+1)%4
		E-=2
	return H