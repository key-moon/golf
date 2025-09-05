def	p(g):
	C=range;E,G=len(g),len(g[0]);D=[]
	for	A	in	C(E):
		if	A==0	or	g[A]!=g[A-1]:D.append([g[A][0]])
	F=[];H=-1
	for	B	in	C(G):
		if	B==0	or	any(g[A][B]!=g[A][B-1]for	A	in	C(E)):F.append(g[0][B])
	if	len(D)>1:return	D
	else:return[F]