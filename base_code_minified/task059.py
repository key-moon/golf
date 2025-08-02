def p(g):
	E=[]
	for B in(0,4,8):
		for C in(0,4,8):
			D=A=0
			for F in range(3):
				for G in range(3):H=g[B+F][C+G];D+=H;A+=H>0
			E+=[(A,D,B,C)]
	I=max(E)[0]
	for(A,D,B,C)in E:
		if A==I:
			for F in range(3):
				for G in range(3):g[B+F][C+G]=D//A
	return g