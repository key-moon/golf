def	p(g):
	h,w=len(g),len(g[0]);v=set();C=[]
	for	i	in	range(h):
		for	j	in	range(w):
			if	g[i][j]==4and(i,j)not	in	v:
				s=[(i,j)];v.add((i,j));k=0
				while	k<len(s):
					a,b=s[k];k+=1
					for(A,B)in(a+1,b),(a-1,b),(a,b+1),(a,b-1):
						if	0<=A<h	and	0<=B<w	and	g[A][B]==4and(A,B)not	in	v:v.add((A,B));s.append((A,B))
				D=min(t[0]for	t	in	s);E=max(t[0]for	t	in	s);F=min(t[1]for	t	in	s);G=max(t[1]for	t	in	s);C.append([(y,x)for	y	in	range(D+1,E)for	x	in	range(F+1,G)])
	for(k,H)in	enumerate(sorted(C,key=len)):
		for(y,x)in	H:g[y][x]=k+1
	return	g