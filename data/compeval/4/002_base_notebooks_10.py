from	collections	import*
def	p(a):
	if	not	a	or	not	a[0]:return[]
	r,c=len(a),len(a[0]);q=deque([(i,j)for	i	in	range(r)for	j	in	range(c)if(i*j==0	or	i==r-1or	j==c-1)and	a[i][j]==0])
	while	q:
		x,y=q.popleft();a[x][y]=1
		for(b,G)in[(0,1),(0,-1),(1,0),(-1,0)]:
			X,u=x+b,y+G
			if	0<=X<r	and	0<=u<c	and	a[X][u]==0:q.append((X,u));a[X][u]=1
	return[[4if	v==0else	0if	v==1else	v	for	v	in	W]for	W	in	a]