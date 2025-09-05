def	p(g):
	A=[];B=[list(r)for	r	in	zip(*g[::-1])];m=[list(r)for	r	in	zip(*B[::-1])];C=[list(r)for	r	in	zip(*m[::-1])]
	for	r	in	range(len(g)):A.append(g[r]+B[r])
	for	r	in	range(len(g)):A.append(C[r]+m[r])
	return	A