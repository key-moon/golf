def	p(m):
	a=[(i,j)for(i,r)in	enumerate(m)for(j,v)in	enumerate(r)if	v]
	if	not	a:return[]
	from	collections	import	Counter	as	A;v=A(m[i][j]for(i,j)in	a).most_common(1)[0][0];x=[(i,j)for(i,j)in	a	if	m[i][j]==v];B,C=min(i	for(i,_)in	x),min(j	for(_,j)in	x);D,E=max(i	for(i,_)in	x)+1,max(j	for(_,j)in	x)+1;return[m[i][C:E]for	i	in	range(B,D)]