def	p(j,A=range):
	c,B=len(j),len(j[0]);j=[[2if	k>0else	0for	k	in	k]for	k	in	j]
	for	k	in	A(B):
		C=[j[c][k]for	c	in	A(c)][::-1];l=sum(C)//2//2
		for	D	in	A(l):j[-(D+1)][k]=8
	return	j