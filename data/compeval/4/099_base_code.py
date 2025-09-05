def	p(g):
	C=set();D=[];E=[];n,m=len(g),len(g[0])
	for	i	in	range(n):
		for	j	in	range(m):
			t=g[i][j]
			if	t==1and(i,j)not	in	C:
				a=c=i;b=d=j;s=[(i,j)];C.add((i,j))
				while	s:
					x,y=s.pop()
					if	x<a:a=x
					if	x>c:c=x
					if	y<b:b=y
					if	y>d:d=y
					for	k	in	1,-1:
						A,B=x+k,y
						if	0<=A<n	and	g[A][B]==1and(A,B)not	in	C:C.add((A,B));s.append((A,B))
						A,B=x,y+k
						if	0<=B<m	and	g[A][B]==1and(A,B)not	in	C:C.add((A,B));s.append((A,B))
				D.append((a,c,b,d))
			elif	t>1:E.append((i,j,t))
	for(i,j,t)in	E:
		for(a,c,b,d)in	D:
			if	a<=i<=c	and	b<=j<=d:
				F=a-1if	a	else	0
				for	x	in	range(F,c+1):
					for	y	in	range(b,d+1):
						if	g[x][y]==0:g[x][y]=t
				break
	return	g