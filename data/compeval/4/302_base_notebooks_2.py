def	p(j):
	C,c=len(j),len(j[0]);A=[[0]*c	for	b	in	j];k=[]
	def	e(W,l):
		B=[(W,l)];A[W][l]=1;a=[(W,l)];D=1
		while	B:
			e,E=B.pop()
			for(w,F)in[(0,1),(1,0),(0,-1),(-1,0)]:
				b,k=e+w,E+F
				if	not(0<=b<C	and	0<=k<c):D=0;continue
				if	j[b][k]<1and	not	A[b][k]:A[b][k]=1;B+=[(b,k)];a+=[(b,k)]
		return	a	if	D	else[]
	for	b	in	range(C):
		for	B	in	range(c-1,-1,-1):
			if	j[b][B]<1and	not	A[b][B]:k+=[e(b,B)]
	k.sort(key=len,reverse=1)
	for(b,a)in	enumerate(k):
		E=min(8,max(6,len(a)**.5+.0+5))
		for	D	in	a:j[D[0]][D[1]]=E
	return	j