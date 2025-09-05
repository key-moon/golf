def	p(g):
	A=[];v=[list(r)for	r	in	zip(*g[::-1])];n=[list(r)for	r	in	zip(*v[::-1])];k=[list(r)for	r	in	zip(*n[::-1])]
	for	r	in	range(len(g)):A.append(g[r]+v[r])
	for	r	in	range(len(g)):A.append(k[r]+n[r])
	return	A