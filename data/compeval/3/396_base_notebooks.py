def	p(j):
	A=range;c,E=len(j),len(j[0]);k={}
	for	F	in	A(c):
		for	l	in	A(E):
			if	j[F][l]:k[j[F][l]]=k.get(j[F][l],0)+1
	D,a=max(k,key=k.get),min(k,key=k.get);G,e=0,None
	for	B	in	A(c-2):
		for	w	in	A(E-2):
			for	C	in	A(B+2,c):
				for	b	in	A(w+2,E):
					if	all(j[B][A]==D	for	A	in	A(w,b+1))and	all(j[C][A]==D	for	A	in	A(w,b+1))and	all(j[A][w]==D	for	A	in	A(B,C+1))and	all(j[A][b]==D	for	A	in	A(B,C+1)):
						d=(C-B+1)*(b-w+1)
						if	d>G:G,e=d,(B,w,C,b)
	B,w,C,b=e;return[[a	if	j[B+C][w+A]==D	else	j[B+C][w+A]for	A	in	A(b-w+1)]for	C	in	A(C-B+1)]