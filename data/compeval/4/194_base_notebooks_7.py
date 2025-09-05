r=lambda	x:[[*i]for	i	in	zip(*x[::-1])]
p=lambda	g:[a+b	for(a,b)in	zip(g,r(g))]+[a+b	for(a,b)in	zip(r(r(r(g))),r(r(g)))]