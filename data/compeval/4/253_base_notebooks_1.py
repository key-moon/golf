def	p(j):
	C=len(j)-1;c=[0]*16
	for	B	in	range(C):
		for	k	in	range(C):
			if(A:=j[B][k])and	j[B+1][k]==A	and	j[B][k+1]==A:c[0]=c[4]=c[1]=A
			if	A	and	j[B+1][k]==A	and	j[B+1][k+1]==A:c[8]=c[12]=c[13]=A
			if	A	and	j[B][k+1]==A	and	j[B+1][k+1]==A:c[2]=c[3]=c[7]=A
			if(l:=j[B+1][k+1])and	j[B+1][k]==l	and	j[B][k+1]==l:c[11]=c[14]=c[15]=l
	return[c[A:A+4]for	A	in(0,4,8,12)]