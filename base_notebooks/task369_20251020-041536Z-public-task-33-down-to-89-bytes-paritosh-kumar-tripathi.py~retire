def p(n):
	B=range;C=set()
	def D(e,d):
		if(e,d)in C or not(0<=e<10 and 0<=d<10)or n[e][d]:return[]
		C.add((e,d));return[(e,d)]+sum([D(e+A,d+B)for(A,B)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for F in B(10):
		for A in B(10):
			E=D(F,A)
			for(G,A)in E:n[G][A]=abs(len(E)-4)
	return n
