from	collections	import*
def	p(a):
	if	not	a	or	not	a[0]:return[]
	r,c=len(a),len(a[0]);q=deque([(i,j)for	i	in	range(r)for	j	in	range(c)if(i*j==0	or	i==r-1or	j==c-1)and	a[i][j]==0])
	while	q:
		x,y=q.popleft();a[x][y]=1
		for(g,n)in[(0,1),(0,-1),(1,0),(-1,0)]:
			k,D=x+g,y+n
			if	0<=k<r	and	0<=D<c	and	a[k][D]==0:q.append((k,D));a[k][D]=1
	return[[4if	v==0else	0if	v==1else	v	for	v	in	X]for	X	in	a]