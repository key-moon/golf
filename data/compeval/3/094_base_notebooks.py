j=len
A=range
def	p(c):
	D,k=[],[];E,l=j(c),j(c[0])
	for	B	in	A(E-4):
		for	a	in	A(l-4):
			C=[[c[A+B][C+a]for	A	in	A(5)]for	C	in	A(5)];C=[a	for	A	in	C	for	a	in	A];C=sum([A	for	A	in	C	if	A==1])
			if	C==16:D.append(B+2);k.append(a+2)
	for	B	in	A(E):
		for	a	in	A(l):
			if	B	in	D	or	a	in	k:
				if	c[B][a]!=1:c[B][a]=6
	return	c