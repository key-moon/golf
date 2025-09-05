def	p(j):
	B=range;c=len(j);C=c//2-2;k=[];E=[j[0][0],j[0][-1],j[-1][0],j[-1][-1]]
	for	l	in	B(2,c-2):
		D=[]
		for	a	in	B(2,c-2):
			A=j[l][a]
			if	A==8:e=(l-2)//C;F=(a-2)//C;A=E[e*2+F]
			D.append(A)
		k.append(D)
	return	k