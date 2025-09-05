def	p(j,A=range):
	c=[A[:]for	A	in	j]
	for	E	in	A(1,10):
		k=[(B,k)for	B	in	A(len(j))for	k	in	A(len(j[0]))if	j[B][k]==E]
		for	D	in	A(len(k)):
			for	l	in	A(D+1,len(k)):
				B,a=k[D];C,e=k[l]
				if	B==C:
					for	F	in	A(min(a,e),max(a,e)+1):c[B][F]=8
				elif	a==e:
					for	w	in	A(min(B,C),max(B,C)+1):c[w][a]=8
		for(B,C)in	k:c[B][C]=1
	return	c