def	p(g):
	h=len(g);w=len(g[0]);v=set()
	for	i	in	range(h):
		for	j	in	range(w):
			if	g[i][j]==6and(i,j)not	in	v:
				s=[(i,j)];v.add((i,j));C=D=i;E=F=j
				while	s:
					y,x=s.pop()
					if	y<C:C=y
					if	x<E:E=x
					if	y>D:D=y
					if	x>F:F=x
					for(G,H)in(1,0),(-1,0),(0,1),(0,-1):
						A,B=y+G,x+H
						if	0<=A<h	and	0<=B<w	and	g[A][B]==6and(A,B)not	in	v:v.add((A,B));s+=[(A,B)]
				C-=1;E-=1;D+=1;F+=1
				for	A	in	range(C,D+1):
					for	B	in	range(E,F+1):
						if	A	in(C,D)or	B	in(E,F):g[A][B]=3
						elif	g[A][B]!=6:g[A][B]=4
	return	g