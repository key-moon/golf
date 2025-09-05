def	p(j,A=range):
	c=[k[:]for	k	in	j];D=set()
	for	k	in	A(len(j)-2):
		for	B	in	A(len(j[0])):
			if	j[k][B]and(k,B)not	in	D:
				l=j[k][B]
				if	all(j[k+A][B]==l	for	A	in	A(3)):
					C=B
					while	C<len(j[0])and	all(j[k+A][C]==l	for	A	in	A(3)):
						for	a	in	A(3):D.add((k+a,C))
						C+=1
					for	E	in	A(B,C):
						if(E-B)%2==1:c[k+1][E]=0
	return	c