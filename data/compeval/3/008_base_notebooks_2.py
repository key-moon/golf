def	p(j,A=enumerate):
	c,B=[(c,b)for(c,B)in	A(j)for(b,d)in	A(B)if	d==2],[(c,b)for(c,B)in	A(j)for(b,d)in	A(B)if	d==8]
	if	not	c	or	not	B:return	j
	k=lambda	W:(min(c	for(c,A)in	W),max(c	for(c,A)in	W),min(c	for(A,c)in	W),max(c	for(A,c)in	W));l,C,a,D=k(c);e,E,w,F=k(B);b=d=0
	if	D<w:d=w-D-1
	elif	F<a:d=F-a+1
	elif	C<e:b=e-C-1
	elif	E<l:b=E-l+1
	f,g={*c},{*B};return[[8if(c,A)in	g	else	2if(c-b,A-d)in	f	else	0for(A,k)in	A(j[0])]for(c,B)in	A(j)]