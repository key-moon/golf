j=len
A=range
def	p(c):
	F,k=j(c),j(c[0]);B=[]
	for	l	in	A(F):
		for	E	in	A(k):
			if	c[l][E]>0:B.append([l,E])
	a=min([A[1]for	A	in	B]);C=max([A[1]for	A	in	B]);e=min([A[0]for	A	in	B]);D=max([A[0]for	A	in	B]);C=C-(C-a)//2;D=D-(D-e)//2;c=c[e:D];c=[A[a:C]for	A	in	c];return	c