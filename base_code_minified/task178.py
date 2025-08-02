def p(g):
	A=[]
	for D in g:
		B=D[0];C=[B]
		for E in D[1:]:
			if E!=B:C+=[(B:=E)]
		if not(A and C==A[-1]):A+=[C]
	return A