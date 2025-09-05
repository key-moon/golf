def	p(j,A=range,c=len):
	C,k=c(j),c(j[0]);j=[[8for	A	in	A]for	A	in	j];B=[A	for	A	in	range(k)];B+=B[::-1][1:-1]
	while	c(B)<C:B+=B[:]
	for	l	in	A(C):j[-(l+1)][B[l]]=1
	return	j