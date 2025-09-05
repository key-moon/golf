def	p(j):
	A=len(j[0]);c=int((A-1)/2);B=enumerate
	for(k,C)in	B(j):
		if	max(C)>0:
			for	l	in	range(c):j[k][l]=j[k][0];j[k][A-l-1]=j[k][A-1]
			j[k][c]=5
	return	j