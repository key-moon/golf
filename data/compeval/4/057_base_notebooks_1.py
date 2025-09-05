def	p(g):
	A=[];C=[]
	for	B	in	g:
		if	max(B)>0:A.append(B)
	for	B	in	A:
		for	i	in	range(len(B)):
			if	B[i]>0:C.append(i)
	A=[A[min(C):max(C)+1]for	A	in	A];A=[A*2for	A	in	A];return	A