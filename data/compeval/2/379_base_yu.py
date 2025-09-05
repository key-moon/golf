E,R=enumerate,range
def	p(g):
	for	_	in	0,1:
		if	l:=[i	for(i,s)in	E(g)if	all(s)]:
			for(i,s)in	E(g):
				for(j,v)in	E(s):
					x,y=l[-(l[-1]<i)],l[-(l[0]<i)]
					for(w,k)in([(x,k)for	k	in	R(x,i)][::-1]+[(y,k)for	k	in	R(i,y+1)])*(v==2):
						for	a	in	R(9):g[w+a//3-1][j+a%3-1]=8
						g[k][j]=2
		*g,=map(list,zip(*g))
	return	g