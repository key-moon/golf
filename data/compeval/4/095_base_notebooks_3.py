def	p(j,A=enumerate):
	for(c,C)in	A(j):
		for(k,D)in	A(C):
			if	D==5:
				for	l	in	range(c-1,c+2):
					for	B	in	range(k-1,k+2):
						if[l,B]!=[c,k]:j[l][B]=1
	return	j