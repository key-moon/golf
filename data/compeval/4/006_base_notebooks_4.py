def	p(m):
	o=[]
	for	r	in	m:
		try:s=r.index(5);l,A=r[:s],r[s+1:];o+=[[2if	l[i]==A[i]==1else	l[i]+A[i]if	l[i]==A[i]else	0for	i	in	range(s)]]
		except:o+=[[]]
	return	o