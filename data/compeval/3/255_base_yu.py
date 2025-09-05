def	p(g):
	c=max(sum(g,[]))
	for	_	in	range(4):
		t=[30]+[[*s,c].index(c)for	s	in	g]+[30];d=set()
		while	True:
			B,A,l,r=max((min(t[l:r])*(r-l-1),min(t[l:r])-1,l,r)for	r	in	range(len(t)+1)for	l	in	range(r-2)if	not{l,r-1}&d)
			if	B<25or	A<5:break
			d|={*range(l,r)};A-=2*(r-l<5)
			for	i	in	range(l,r-2):g[i][:A]=[3]*A
		*g,=map(list,zip(*g[::-1]))
	return	g