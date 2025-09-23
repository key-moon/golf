def p(j):
	C,D,E=len(j),len(j[0]),range;F=[(A,B)for A in(0,C-1)for B in E(D)if j[A][B]<1]+[(A,B)for A in E(C)for B in(0,D-1)if j[A][B]<1]
	while F:
		A,B=F.pop()
		if j[A][B]<1:j[A][B]=3;F+=[(A,B)for(A,B)in((A+1,B),(A-1,B),(A,B+1),(A,B-1))if 0<=A<C and 0<=B<D and j[A][B]<1]
	for A in E(C):
		for B in E(D):
			if j[A][B]<1:j[A][B]=2
	return j