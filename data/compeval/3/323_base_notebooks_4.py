def	p(j):
	C,c=len(j),len(j[0]);B=[A[:]for	A	in	j];k,D=next((k,A)for	k	in	range(C)for	A	in	range(c)if	j[k][A])
	for(l,E)in(-1,1),(1,-1):
		a,A=k,D
		while	1:
			for	e	in[0]*2:
				a+=l
				if	0<=a<C:B[a][A]=5
				else:break
			else:
				for	e	in[0]*2:
					A+=E
					if	0<=A<c:B[a][A]=5
					else:break
				else:continue
			break
	return	B