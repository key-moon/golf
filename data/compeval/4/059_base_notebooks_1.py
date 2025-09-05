def	p(g,E=enumerate,N=range(11)):
	o=0;B=[[0if(i+1)%4>0and(j+1)%4>0else	5for	i	in	N]for	j	in	N];d={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0}
	for(r,C)in	E(g):
		for(c,A)in	E(C):
			if	A>0and	A!=5:o=int(A);d[str(r//4)+str(c//4)]+=1
	m=max(d.values())
	for(r,C)in	E(B):
		for(c,A)in	E(C):
			if	A==0and	d[str(r//4)+str(c//4)]==m:B[r][c]=o
	return	B