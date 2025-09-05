from	itertools	import	product
def	p(j,A=range):
	for(c,B)in	product(A(len(j)-2),A(len(j[0])-2)):
		k=A(c,c+3)
		if	not	all(4in	i	for	i	in[j[c][B:B+3],j[c+2][B:B+3],[j[A][B]for	A	in	k],[j[A][B+2]for	A	in	k]]):continue
		for(C,l)in	product(k,A(B,B+3)):j[C][l]+=7*(j[C][l]==0)
	return	j