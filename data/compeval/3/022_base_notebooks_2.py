j=len
A=range
def	p(c):
	D=[[0,0,0]for	l	in	A(3)];k,E=j(c),j(c[0])
	for	l	in	A(k):
		for	B	in	A(E):
			if	c[l][B]==5:
				for	a	in	A(-1,2):
					for	C	in	A(-1,2):
						if	l+a>=0and	B+C>=0and	c[l+a][B+C]!=0:D[1+a][1+C]=c[l+a][B+C]
	return	D