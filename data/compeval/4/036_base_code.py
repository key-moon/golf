def	p(g):
	n,m=len(g),len(g[0]);v=set();A=set();D=0
	for	i	in	range(n):
		for	j	in	range(m):
			if	g[i][j]and(i,j)not	in	v:
				c=g[i][j];q=[(i,j)];v.add((i,j));s={(i,j)}
				while	q:
					x,y=q.pop()
					for(E,F)in(1,0),(-1,0),(0,1),(0,-1):
						B,C=x+E,y+F
						if	0<=B<n	and	0<=C<m	and	g[B][C]==c	and(B,C)not	in	v:v.add((B,C));q.append((B,C));s.add((B,C))
				if	len(s)>len(A):A=s;D=c
	G,H=min(i	for(i,j)in	A),max(i	for(i,j)in	A);I,J=min(j	for(i,j)in	A),max(j	for(i,j)in	A);return[[D	if(i,j)in	A	else	0for	j	in	range(I,J+1)]for	i	in	range(G,H+1)]