def	p(g):
	A=range;r=[x[:]for	x	in	g];v=set()
	for	p	in[(i,j)for	i	in	A(7)for	j	in	A(7)if	g[i][j]==8and(i,j)not	in	v]:
		c,q=[p],[p];v|={p}
		while	q:x,y=q.pop();c+=[(a,b)for(d,e)in[(0,1),(1,0),(0,-1),(-1,0)]if	0<=(a:=x+d)<7and	0<=(b:=y+e)<7and	g[a][b]==8and(a,b)not	in	v	and	not(v.add((a,b))or	q.append((a,b)))]
		if	len(c)==3:
			i,j=zip(*c)
			for	x	in	A(min(i),max(i)+1):
				for	y	in	A(min(j),max(j)+1):r[x][y]=r[x][y]or	1
	return	r