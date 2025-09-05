def	p(g):
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v==3:a,b=i,j
			if	v==4:c,d=i,j
	A=(c>a)-(c<a);B=(d>b)-(d<b);g[a][b]=0;g[a+A][b+B]=3;return	g