def	p(j):
	for	A	in	range(len(j[0])):
		if	j[-1][A]==2:
			c=0
			for	B	in	range(len(j)):
				if	j[-(B+1)][A+c]==5:c+=1;j[-B][A+c]=2
				j[-(B+1)][A+c]=2
	return	j