def	p(g,L=len,R=range):
	s=R(L([x	for	x	in	set(g[0])if	x>0])*5);A=[[0for	x	in	s]for	y	in	s];g=g[0];B=0
	for	r	in	s:
		for	c	in	R(5):
			try:A[-(r+1)][c+B]=g[c]
			except:pass
		B+=1
	return	A