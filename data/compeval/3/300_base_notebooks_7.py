def	p(m):
	A=enumerate;a=[(i,j)for(i,r)in	A(m)for(j,v)in	A(r)if	v]
	if	not	a:return[]
	from	collections	import	Counter	as	B;v=B(m[i][j]for(i,j)in	a).most_common(1)[0][0];x=[(i,j)for(i,j)in	a	if	m[i][j]==v];g,b=min(i	for(i,_)in	x),min(j	for(_,j)in	x);C,D=max(i	for(i,_)in	x)+1,max(j	for(_,j)in	x)+1;return[m[i][b:D]for	i	in	range(g,C)]