def p(A):
	F=[]
	for C in(0,4,8):
		for D in(0,4,8):
			E=B=0
			for G in range(3):
				for H in range(3):I=A[C+G][D+H];E+=I;B+=I>0
			F+=[(B,E,C,D)]
	J=max(F)[0]
	for(B,E,C,D)in F:
		if B==J:
			for G in range(3):
				for H in range(3):A[C+G][D+H]=E//B
	return A