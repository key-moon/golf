def	p(j):
	A=range;c,C=len(j),len(j[0]);k=[k	for	k	in	A(c)if	all(j[k][A]==0for	A	in	A(C))];B=[k	for	k	in	A(C)if	all(j[A][k]==0for	A	in	A(c))];k=[-1]+k+[c];B=[-1]+B+[C];l=[]
	for	D	in	A(len(k)-1):
		a=[]
		for	E	in	A(len(B)-1):
			for	e	in	A(k[D]+1,k[D+1]):
				for	F	in	A(B[E]+1,B[E+1]):
					if	j[e][F]:a.append(j[e][F]);break
				else:continue
				break
		if	a:l.append(a)
	return	l