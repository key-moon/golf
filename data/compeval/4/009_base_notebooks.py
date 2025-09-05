def	p(j,A=range,c=len):
	F=[A[:]for	A	in	j];k,G=c(j),c(j[0]);l=j[0][2]
	for	B	in	A(k):
		for	a	in	A(G):
			if	j[B][a]==l:F[B][a]=l;j[B][a]=0
			else:F[B][a]=0
	C=[A[:]for	A	in	j]
	for	e	in	A(k):
		D=[(B,a)for	B	in	A(k)for	a	in	A(G)if	j[B][a]==e]
		for	B	in	A(len(D)):
			for	a	in	A(B+1,len(D)):
				w,E=D[B];b,d=D[a]
				if	w==b:
					for	f	in	A(min(E,d),max(E,d)+1):C[w][f]=e
				elif	E==d:
					for	g	in	A(min(w,b),max(w,b)+1):C[g][E]=e
	for	B	in	A(k):
		for	a	in	A(G):
			if	F[B][a]>0:C[B][a]=l
	return	C