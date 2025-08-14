def	p(j,A=enumerate):
	for(c,C)in	A(j):
		for(k,D)in	A(C):
			for(l,B)in(c+1,k),(c-1,k),(c,k+1),(c,k-1):
				if	D==2and	0<=l<len(j)and	0<=B<len(C)and	j[l][B]==3:j[c][k]=0;j[l][B]=8
	return	j