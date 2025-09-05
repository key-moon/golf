def	p(g,R=enumerate):
	a,b=[(i,j)for(i,r)in	R(g)for(j,v)in	R(r)if	v==2],[(i,j)for(i,r)in	R(g)for(j,v)in	R(r)if	v==8]
	if	not	a	or	not	b:return	g
	f=lambda	s:(min(i	for(i,_)in	s),max(i	for(i,_)in	s),min(j	for(_,j)in	s),max(j	for(_,j)in	s));C,D,E,F=f(a);G,H,I,x=f(b);A=B=0
	if	F<I:B=I-F-1
	elif	x<E:B=x-E+1
	elif	D<G:A=G-D-1
	elif	H<C:A=H-C+1
	u,J=set(a),set(b);return[[8if(i,j)in	J	else	2if(i-A,j-B)in	u	else	0for	j	in	range(len(g[0]))]for	i	in	range(len(g))]