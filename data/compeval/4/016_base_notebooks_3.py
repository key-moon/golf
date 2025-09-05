def	p(g):
	d={0:7,1:5,2:6,3:4,4:3,5:1,6:2,7:0,8:9,9:8};A=enumerate
	for(r,B)in	A(g):
		for(c,C)in	A(B):g[r][c]=d[C]
	return	g