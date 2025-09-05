def	p(j):
	C,c=len(j),len(j[0]);A=[[0]*c	for	_	in	j];k=[]
	def	f(W,l):
		B=[(W,l)];A[W][l]=1;a=[(W,l)];D=1
		while	B:
			e,E=B.pop()
			for(w,F)in[(0,1),(1,0),(0,-1),(-1,0)]:
				p,b=e+w,E+F
				if	not(0<=p<C	and	0<=b<c):D=0;continue
				if	j[p][b]<1and	not	A[p][b]:A[p][b]=1;B+=[(p,b)];a+=[(p,b)]
		return	a	if	D	else[]
	for	B	in	range(C):
		for	l	in	range(c-1,-1,-1):
			if	j[B][l]<1and	not	A[B][l]:k+=[f(B,l)]
	k.sort(key=len,reverse=1)
	for(B,e)in	enumerate(k):
		d=min(8,max(6,len(e)**.5+.0+5))
		for	D	in	e:j[D[0]][D[1]]=d
	return	j