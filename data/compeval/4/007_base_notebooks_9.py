def	p(g,E=enumerate):
	m=len({*sum(g,[])}-{0});s=[0]*m
	for(i,r)in	E(g):
		for(j,v)in	E(r):
			if	v:s[(i+j)%m]=v
	return[[s[(i+j)%m]for(j,_)in	E(r)]for(i,r)in	E(g)]