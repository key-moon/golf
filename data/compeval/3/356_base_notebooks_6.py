def	p(j,A=range):
	c=[r[:]for	r	in	j]
	for	C	in	A(1,10):
		k=[(B,l)for	B	in	A(len(j))for	l	in	A(len(j[0]))if	j[B][l]==C]
		for	E	in	A(len(k)):
			for	l	in	A(E+1,len(k)):
				B,a=k[E];D,e=k[l]
				if	B==D:
					for	F	in	A(min(a,e),max(a,e)+1):c[B][F]=C
				elif	a==e:
					for	w	in	A(min(B,D),max(B,D)+1):c[w][a]=C
	return	c