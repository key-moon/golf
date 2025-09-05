def	p(g):
	A={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:A[v]=A.get(v,0)+1
	G=max(A,key=A.get);B=C=99;D=E=0
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==G:
				if	i<B:B=i
				if	i>D:D=i
				if	j<C:C=j
				if	j>E:E=j
	H=[]
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v	and	v!=G:H+=i,j,v;g[i][j]=0
	F=iter(H)
	for(i,j,v)in	zip(F,F,F):x=D+1if	i==B+1else	B-1;y=E+1if	j==C+1else	C-1;g[x][y]=v
	return	g