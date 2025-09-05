from	collections	import*
def	p(m):
	r,c=len(m),len(m[0]);v=set();a=0;z=0
	for	i	in	range(r):
		for	j	in	range(c):
			if	m[i][j]<1and(i,j)not	in	v:
				q=deque([(i,j)]);v|={(i,j)};A={(i,j)};b=set();e=1;en=1
				while	q:
					x,y=q.popleft()
					for(u,vv)in[(0,1),(1,0),(-1,0),(0,-1)]:
						X,Y=x+u,y+vv
						if	not	0<=X<r>Y>=0:en=0;continue
						if(X,Y)in	A:continue
						A|={(X,Y)}
						if	m[X][Y]:b|={m[X][Y]}
						else:q.append((X,Y));v|={(X,Y)}
						e+=1
				if	en	and	e>a	and	len(b)==1:a=e;z=b.pop()
	return[[z]*2]*2