def	p(j,A=enumerate):
	c=range;D=len(j);k=len(j[0]);E=lambda	l,J:l==J	or	l*J<1;a=next((w	for	w	in	c(1,k)if	all(E(b,B)for	A	in	j	for(b,B)in	zip(A,A[w:]))),k);F=next((w	for	w	in	c(1,D)if	all(E(b,B)for(w,A)in	zip(j,j[w:])for(b,B)in	zip(w,A))),D);e={}
	for(C,w)in	A(j):
		for(B,b)in	A(w):
			if	b:e[C%F,B%a]=b
	for(C,w)in	A(j):
		for(B,b)in	A(w):
			if	not	b:w[B]=e[C%F,B%a]
	return	j