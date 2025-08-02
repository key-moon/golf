def p(g):
	E,F=len(g),len(g[0]);H=sum(g,[]);I=list({*H}-{0});G=[A for A in I if H.count(A)==1][0];J=[A for A in I if A!=G][0]
	for A in range(E):
		for B in range(F):
			if g[A][B]==G:break
			else:break
	for(C,D)in[(-1,0),(1,0),(0,-1),(0,1)]:
		if 0<=A+C<E and 0<=B+D<F and g[A+C][B+D]==J:C,D=-C,-D;break
	while 0<=A+C<E and 0<=B+D<F:A+=C;B+=D;g[A][B]=G
	return g