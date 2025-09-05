from	collections	import	Counter
def	p(g):
	b=[x	for	A	in	g	for	x	in	A];A=Counter(b).most_common(3);A=[c	for	c	in	A	if	c[0]>0][-1][0];g=[B	for	B	in	g	if	A	in	B];B=[]
	for	C	in	g:
		for	i	in	range(len(C)):
			if	C[i]==A:B.append(i)
	g=[A[min(B):max(B)+1]for	A	in	g];return	g