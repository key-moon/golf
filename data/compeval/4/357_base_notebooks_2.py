def	p(g,R=range,L=len):
	h,w=L(g),L(g[0]);g=[[8for	i	in	r]for	r	in	g];A=[i	for	i	in	range(w)];A+=A[::-1][1:-1]
	while	L(A)<h:A+=A[:]
	for	r	in	R(h):g[-(r+1)][A[r]]=1
	return	g