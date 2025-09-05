def	p(j,A=len,c=enumerate,E=min,k=max,W=range):
	l,F=A(j),A(j[0]);a=[(A,b)for(A,f)in	c(j)for(b,B)in	c(f)if	B==5];D=E(A	for(A,f)in	a);e=k(A	for(A,f)in	a);C=E(A	for(f,A)in	a);w=k(A	for(f,A)in	a)
	for	B	in	range(D+1,e):j[B][C+1:w]=[8]*(w-C-1)
	b=None;d=0,0
	for	f	in	W(C,w+1):
		if	j[D][f]==0:b=D,f;d=-1,0;break
	if	not	b:
		for	f	in	range(C,w+1):
			if	j[e][f]==0:b=e,f;d=1,0;break
	if	not	b:
		for	B	in	range(D,e+1):
			if	j[B][C]==0:b=B,C;d=0,-1;break
	if	not	b:
		for	B	in	range(D,e+1):
			if	j[B][w]==0:b=B,w;d=0,1;break
	B,f=b;g,h=d
	while	0<=B<l	and	0<=f<F	and	j[B][f]==0:j[B][f]=8;B+=g;f+=h
	return	j