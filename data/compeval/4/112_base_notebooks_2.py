def	p(j,h=enumerate):
	C=c=0
	for(A,k)in	h(j):
		for(B,l)in	h(k):C+=A*(l==3);c+=B*(l==3)
	C//=2;c//=2
	for(A,k)in	h(j):
		for(B,l)in	h(k):
			if	l==2:
				for(D,a)in(A,B),(C-A,B),(A,c-B),(C-A,c-B):j[D][a]=2
	return	j