A=range
p=lambda	g:[[max(c	for	r	in	g[i%10::10]for	c	in	r[j%10::10])for	j	in	A(len(g[0]))]for	i	in	A(len(g))]