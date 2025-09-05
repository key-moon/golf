def	p(g):
	A=[];v=[list(r)for	r	in	zip(*g[::-1])];B=[list(r)for	r	in	zip(*v[::-1])];C=[list(r)for	r	in	zip(*B[::-1])]
	for	r	in	range(len(g)):A.append(g[r]+v[r])
	for	r	in	range(len(g)):A.append(C[r]+B[r])
	return	A