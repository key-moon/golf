B=range
def	p(j,A=enumerate):
	for(c,D)in	A(j):
		for(k,E)in	A(D):
			if	E==5:
				for	l	in	B(c-1,c+2):
					for	C	in	B(k-1,k+2):
						if[l,C]!=[c,k]:j[l][C]=1
	return	j