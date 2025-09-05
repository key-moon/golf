def	p(j,A=range):
	c,E=len(j),len(j[0]);p=[(l,B,j[l][B])for	l	in	A(c)for	B	in	A(E)if	j[l][B]];p.sort()
	if	len(p)==2:
		k,C=p
		if	k[0]==C[0]:
			l,F,a=k;D,e=C[1],C[2];B=abs(D-F)
			for	w	in	A(c):j[w][F]=a;j[w][D]=e
			if	B:
				G=max(F,D)+B;b=0;d=[a,e]
				if	D<F:d=d[::-1]
				while	G<E:
					for	w	in	A(c):j[w][G]=d[b%2]
					G+=B;b+=1
		elif	k[1]==C[1]:
			G,f,a=k[1],k[0],k[2];g,e=C[0],C[2];B=abs(g-f)
			for	w	in	A(E):j[f][w]=a;j[g][w]=e
			if	B:
				l=g+B;b=0;d=[a,e]
				while	l<c:
					for	w	in	A(E):j[l][w]=d[b%2]
					l+=B;b+=1
		elif	k[0]==0and	C[0]==c-1:
			f,F,a=k;g,D,e=C;B=abs(D-F)
			for	w	in	A(c):j[w][F]=a;j[w][D]=e
			if	B:
				G=D+B;b=0;d=[a,e]
				while	G<E:
					for	w	in	A(c):j[w][G]=d[b%2]
					G+=B;b+=1
		elif	k[1]==0and	C[1]==E-1or	C[1]==0and	k[1]==E-1:
			if	k[1]==0:f,F,a=k;g,D,e=C
			else:f,F,a=C;g,D,e=k
			B=abs(g-f)
			for	w	in	A(E):j[f][w]=a;j[g][w]=e
			if	B:
				l=max(f,g)+B;b=0;d=[a,e]
				if	g<f:d=d[::-1]
				while	l<c:
					for	w	in	A(E):j[l][w]=d[b%2]
					l+=B;b+=1
	return	j