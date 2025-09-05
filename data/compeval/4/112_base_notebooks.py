def	p(j,p=enumerate):
	C=c=0
	for(A,k)in	p(j):
		for(B,l)in	p(k):C+=A*(l==3);c+=B*(l==3)
	C//=2;c//=2
	for(A,k)in	p(j):
		for(B,l)in	p(k):
			if	l==2:
				for(D,a)in(A,B),(C-A,B),(A,c-B),(C-A,c-B):j[D][a]=2
	return	j