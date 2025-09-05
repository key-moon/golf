def	p(j):
	C=range;c=len;E=[A[:]for	A	in	j];k=set()
	for	A	in	C(c(j)):
		for	l	in	C(c(j[0])):
			if	j[A][l]and(A,l)not	in	k:
				B,a=[(A,l)],[(A,l)];k.add((A,l));F=j[A][l]
				while	a:
					e,D=a.pop()
					for(w,G)in[(0,1),(1,0),(0,-1),(-1,0)]:
						b,d=e+w,D+G
						if	0<=b<c(j)and	0<=d<c(j[0])and	j[b][d]==F	and(b,d)not	in	k:k.add((b,d));B.append((b,d));a.append((b,d))
				f=min(A[0]for	A	in	B);g=max(A[0]for	A	in	B);h=min(A[1]for	A	in	B);i=max(A[1]for	A	in	B)
				for	e	in	C(f+1,g):
					for	D	in	C(h+1,i):E[e][D]=8
	return	E