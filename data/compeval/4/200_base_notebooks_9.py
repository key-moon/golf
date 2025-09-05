def	p(j):
	A,c,B,k=10,enumerate,range,0
	for(E,l)in	c(j):
		for(D,a)in	c(l):
			if	a%5:
				for	C	in	B(D,A,2):
					for	e	in	B(E+1):j[e][C]=a
				for	C	in	B(D+1,A,2):j[k*(A-1)][C]=5;k^=1
				return	j