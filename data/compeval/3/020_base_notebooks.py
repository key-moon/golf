def	p(g,H=enumerate):
	t=l=9**9;b=r=-1
	for(y,a)in	H(g):
		for(x,v)in	H(a):
			if	v:t=min(t,y);b=max(b,y);l=min(l,x);r=max(r,x)
	s=t+b;F=l+r
	for	y	in	range(t,b+1):
		for	x	in	range(l,r+1):
			A=s-y;B=F-x;u=t+x-l;v=l+y-t;C=t+r-x;D=l+b-y;E=(y,x),(y,B),(A,x),(A,B),(u,v),(C,v),(u,D),(C,D);c=max(g[i][j]for(i,j)in	E)
			for(i,j)in	E:g[i][j]=c
	return	g