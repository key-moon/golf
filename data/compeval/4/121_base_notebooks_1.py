def	p(j):
	for	A	in	range(1,len(j)-1):
		for	c	in	range(1,len(j[0])-1):
			if	j[A][c]==8:
				B=[]
				for	k	in[-1,0,1]:
					for	C	in[-1,0,1]:
						if(k	or	j)and	j[A+k][c+C]:B.append(j[A+k][c+C])
				l=max(set(B),key=B.count);D=[[j[A+B][c+k]for	k	in[-1,0,1]]for	B	in[-1,0,1]];D[1][1]=l;return	D