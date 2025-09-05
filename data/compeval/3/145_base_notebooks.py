def	p(j):
	F=[A[:]for	A	in	j];c,G=len(j),len(j[0]);k=set();C=[]
	for	l	in	range(c):
		for	D	in	range(G):
			if	j[l][D]!=2and(l,D)not	in	k:
				a,E=[],[(l,D)];k.add((l,D));e=0
				while	E:
					A,w=E.pop();a.append((A,w))
					if	j[A][w]==0:e+=1
					for(B,b)in[(0,1),(1,0),(0,-1),(-1,0)]:
						if	0<=A+B<c	and	0<=w+b<G	and	j[A+B][w+b]!=2and(A+B,w+b)not	in	k:k.add((A+B,w+b));E.append((A+B,w+b))
				C.append((e,a))
	d=max(A[0]for	A	in	C);f=min(A[0]for	A	in	C)
	for(e,a)in	C:
		k=1if	e==d	else	8if	e==f	else	0
		if	k:
			for(A,w)in	a:
				if	j[A][w]==0:F[A][w]=k
	return	F