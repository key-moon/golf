def	p(j,A=enumerate):
	c=B=0
	for(k,D)in	A(j):
		for(l,C)in	A(D):c+=k*(C==3);B+=l*(C==3)
	c//=2;B//=2
	for(k,D)in	A(j):
		for(l,C)in	A(D):
			if	C==2:
				for(a,E)in(k,l),(c-k,l),(k,B-l),(c-k,B-l):j[a][E]=2
	return	j