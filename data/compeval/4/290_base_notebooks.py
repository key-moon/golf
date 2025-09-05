def	p(g):
	g=[A	for	A	in	g	if	sum(A)>0];B=[];A=[]
	for	C	in	g:
		for	i	in	range(len(C)):
			if	C[i]>0:B.append(i);A.append(C[i])
	A=list(set(A));A={A[0]:A[1],A[1]:A[0]};g=[A[min(B):max(B)+1]for	A	in	g];g=[[A[c]for	c	in	B]for	B	in	g];return	g