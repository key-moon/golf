def	p(j):
	A=[[0]*3,[0]*3,[0]*3]
	for	c	in	range(16):B,k=c//8%2*-2+c//2%2,c//4%2*-2+c%2;A[B][k]=max(A[B][k],j[B][k])
	return	A