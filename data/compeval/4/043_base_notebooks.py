def	p(j,A=enumerate):
	c=len(j)-1;B=len(j[0])-1
	for(k,C)in	A(j):
		for(l,D)in	A(C):
			if	k>0and	l<c:
				if	j[k][B]==5and	j[0][l]==5:j[k][l]=2
	return	j