def	p(j):
	A=range;c=(len(j)-1)//2
	if	c==1:
		B=[j[0][0],j[0][2],j[2][0],j[2][2]]
		for	k	in	B:
			if	B.count(k)==1:return[[k]]
	for(D,l)in[(0,0),(0,c+1),(c+1,0),(c+1,c+1)]:
		C=[[j[D+k][l+c]for	c	in	A(c)]for	k	in	A(c)];k=[C[k][B]for	k	in	A(c)for	B	in	A(c)]
		if	len(set(k))>1:return	C