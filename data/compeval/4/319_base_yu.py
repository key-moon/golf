def	p(g):
	*C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
	for	c	in	C:
		for	y	in	range(-32,14):
			for	x	in	range(-32,14):
				A=[];B=[];d=[]
				for	i	in	range(len(g)):
					for	j	in	range(len(g[i])):
						if	g[i][j]==c:
							A+=[i];B+=[j]
							for	k	in	range(2):
								for	l	in	range(2):
									D=i*2+y+k;E=j*2+x+l
									if	len(g)>D>-1<E<len(g[i]):d+=[g[D][E]]
				B,*_,F=sorted(B);A,*_,G=sorted(A)
				if	any({*d}=={C[k]}and	len(d)==sum(g,[]).count(C[k])for	k	in	range(3)):return[[[b,c][v==c]for	v	in	s[B:F+1]]for	s	in	g[A:G+1]]