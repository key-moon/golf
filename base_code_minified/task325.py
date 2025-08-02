def p(A):
	B={A+C*1j for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D};C=0
	while B:
		D=[B.pop()]
		while D:
			E=D.pop()
			for F in(1,-1,1j,-1j):
				if E+F in B:B.remove(E+F);D.append(E+F)
		C+=1
	return[[8*(A==B)for B in range(C)]for A in range(C)]