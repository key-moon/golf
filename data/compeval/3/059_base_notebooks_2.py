def	p(g):
	o=0;C=[[0if(i+1)%4>0and(j+1)%4>0else	5for	i	in	range(11)]for	j	in	range(11)];d={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0};B=enumerate
	for(r,D)in	B(g):
		for(c,A)in	B(D):
			if	A>0and	A!=5:o=int(A);d[str(r//4)+str(c//4)]+=1
	m=max([d[k]for	k	in	d])
	for(r,D)in	B(C):
		for(c,A)in	B(D):
			if	A==0and	d[str(r//4)+str(c//4)]==m:C[r][c]=o
	return	C