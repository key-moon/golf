def	p(g,u=range):
	E=enumerate;B=[[A	for(i,A)in	E(A)]for	A	in	g];C,A=[],[]
	for	r	in	u(len(g)):
		for	c	in	u(len(g[0])):
			try:
				if	g[r-1][c]==5and	g[r][c]==8:B[r][c]=5
			except:pass
			try:
				if	g[r+1][c]==5and	g[r][c]==8:B[r][c]=5
			except:pass
	for	i	in	u(len(B)):
		if	5in	B[i]:A.append(g[i])
	for	D	in	A:
		for	i	in	u(len(D)):
			if	D[i]==5:C.append(i)
	A=[A[min(C):max(C)+1]for	A	in	A];return	A