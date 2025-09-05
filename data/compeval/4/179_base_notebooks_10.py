def	p(g):
	h,w=len(g),len(g[0]);b=[]
	for	i	in	range(0,h,3):
		for	j	in	range(0,w,1):
			for	E	in	range(3):
				for	F	in	range(1):b.append(g[i+E][j+F])
	B,A=3,3;C=[[0]*A	for	_	in	range(B)]
	for(D,v)in	enumerate(b[:B*A]):C[D//A][D%A]=v
	return	C