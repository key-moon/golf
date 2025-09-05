def	p(g):
	n=len(g);A=range(n*n)
	for	v	in[e:=1,1,1,0]*2:
		a,b,*_=[A	for	A	in	A	if	g[A//n][A%n]==3];y=[A	for	A	in	A	if	g[A//n][A%n]==2][0];l=r=[*g[b//n],8].index(8,b%n);u=[*[s[r-1]for	s	in	g],8].index(8,b//n);w=y%n
		if	l>w:l,w=w+2,l
		if(abs(a-b)==e)*(u==y//n+1)*~-(8*(r<n)in	g[y//n][l:w]):
			g[b//n][b%n+1:r]=[3]*(r-b%n-1)
			for	s	in	g[b//n:u]:s[r-1]=e=3
			g[y//n][l:w]=[3]*(w-l)
		if	v:g=g[::-1]
		*g,=map(list,zip(*g))
	return	g