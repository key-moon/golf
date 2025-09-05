from	collections	import*
def	p(a):
	if	not	a	or	not	a[0]:return[]
	r,c=len(a),len(a[0]);q=deque([(i,j)for	i	in	range(r)for	j	in	range(c)if(i*j==0	or	i==r-1or	j==c-1)and	a[i][j]==0])
	while	q:
		x,y=q.popleft();a[x][y]=1
		for(N,m)in[(0,1),(0,-1),(1,0),(-1,0)]:
			s,A=x+N,y+m
			if	0<=s<r	and	0<=A<c	and	a[s][A]==0:q.append((s,A));a[s][A]=1
	return[[4if	v==0else	0if	v==1else	v	for	v	in	F]for	F	in	a]