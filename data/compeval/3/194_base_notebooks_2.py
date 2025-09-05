def	p(g):
	A=[];B=[list(r)for	r	in	zip(*g[::-1])];C=[list(r)for	r	in	zip(*B[::-1])];b=[list(r)for	r	in	zip(*C[::-1])]
	for	r	in	range(len(g)):A.append(g[r]+B[r])
	for	r	in	range(len(g)):A.append(b[r]+C[r])
	return	A