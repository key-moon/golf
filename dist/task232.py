def	p(j,A=enumerate):
	for(c,C)in	A(j):
		k,B,l=0,[],0
		for(D,a)in	A(C):
			if	a>0:B=[a,5]*20;l=1
			if	l:j[c][D]=B[k];k+=1
	return	j