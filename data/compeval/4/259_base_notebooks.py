def	p(j,A=range):
	c,E=len(j),len(j[0]);k,C,l,D=c,0,E,0
	for	a	in	A(c):
		for	B	in	A(E):
			if	j[a][B]-1:
				if	a<k:k=a
				if	a>C:C=a
				if	B<l:l=B
				if	B>D:D=B
	return[[x-(x==1)for	x	in	r[l:D+1]]for	r	in	j[k:C+1]]