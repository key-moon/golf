def	p(g):
	A=[];j=[list(r)for	r	in	zip(*g[::-1])];b=[list(r)for	r	in	zip(*j[::-1])];u=[list(r)for	r	in	zip(*b[::-1])]
	for	r	in	range(len(g)):A.append(g[r]+j[r])
	for	r	in	range(len(g)):A.append(u[r]+b[r])
	return	A