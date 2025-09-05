def	p(j,v=enumerate):
	C=range;c=len(j);D=len(j[0]);k=lambda	W,l:W==l	or	W*l<1;E=next((A	for	A	in	C(1,D)if	all(k(B,e)for	w	in	j	for(B,e)in	zip(w,w[A:]))),D);a=next((A	for	A	in	C(1,c)if	all(k(B,e)for(A,w)in	zip(j,j[A:])for(B,e)in	zip(A,w))),c);F={}
	for(e,A)in	v(j):
		for(w,B)in	v(A):
			if	B:F[e%a,w%E]=B
	for(e,A)in	v(j):
		for(w,B)in	v(A):
			if	not	B:A[w]=F[e%a,w%E]
	return	j