def p(g):
	for(E,B)in enumerate(g):
		A=[-1]
		for(C,F)in enumerate(B):
			if F==2:A+=[C]
		A+=[len(B)]
		for D in range(len(A)-1):
			if D%3==2*(E<1):
				for C in range(A[D]+1,A[D+1]):B[C]=4
	return g