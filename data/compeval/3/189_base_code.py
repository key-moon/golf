def	p(g):
	for(A,D)in	enumerate(g):
		if	D.count(8)==len(D):break
	for(B,E)in	enumerate(zip(*g)):
		if	E.count(8)==len(E):break
	F=[[r[:B]for	r	in	g[:A]],[r[B+1:]for	r	in	g[:A]],[r[:B]for	r	in	g[A+1:]],[r[B+1:]for	r	in	g[A+1:]]];I=next(x	for	x	in	F	if	len(x)==2and	len(x[0])==2);C=next(x	for	x	in	F	if	len(x)>2and	len(x[0])>2);G,H=len(C),len(C[0]);J,K=G//2,H//2;return[[C[i][j]//3*I[i//J][j//K]for	j	in	range(H)]for	i	in	range(G)]