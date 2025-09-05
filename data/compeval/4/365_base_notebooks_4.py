def	p(j):
	C,c=len(j),len(j[0]);D=-1
	for	k	in	range(C):
		for	A	in	range(c):
			if	j[k][A]and(k<1or	j[k-1][A]<1)and(A<1or	j[k][A-1]<1):
				l=B=1
				while	A+l<c	and	j[k][A+l]:l+=1
				while	k+B<C	and	j[k+B][A]:B+=1
				a=[B[A:A+l]for	B	in	j[k:k+B]];E=sum(z.count(2)for	z	in	a)
				if	E>D:D=E;e=a
	return	e