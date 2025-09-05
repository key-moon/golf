def	p(j):
	C=range;c=[a[:]for	a	in	j];F=[(0,1),(1,0),(0,-1),(-1,0)];k=[(-1,-1),(-1,1),(1,1),(1,-1)]
	for	A	in	C(10):
		for	l	in	C(10):
			if	j[A][l]and	all(0<=A+a<10and	0<=l+B<10and	j[A+a][l+B]==0for(a,B)in	F):
				for	B	in	k:
					a,D=A+B[0],l+B[1]
					if	0<=a<10and	0<=D<10and	j[a][D]:
						e,G=-B[0],-B[1]
						for	w	in	C(1,10):
							E,b=A+e*w,l+G*w
							if	0<=E<10and	0<=b<10:c[E][b]=j[A][l]
	return	c