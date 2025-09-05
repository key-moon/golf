def	p(j,A=range):
	c=3;B=[]
	for	k	in	A(len(j[0])):
		for	C	in	A(len(j)):
			if	j[C][k]:B.append(j[C][k]);break
	B+=[0]*(c*c-len(B));return[B[k*c:(k+1)*c]if	k%2==0else	B[k*c:(k+1)*c][::-1]for	k	in	A(c)]