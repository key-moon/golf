A=lambda	g,x:sum(sum(i==x	for	i	in	r)for	r	in	g)
def	p(g):a=max(A([r],8)for	r	in	g);q=(A(g,5)-a-2)/2-A(g,8)/a;return[[8*(q>0),8*(q>1),8*(q>2)],[0,0,8*(q>3)],[0,0,0]]