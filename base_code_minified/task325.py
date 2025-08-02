def p(g):
	A={A+C*1j for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D};B=0
	while A:
		C=[A.pop()]
		while C:
			D=C.pop()
			for E in(1,-1,1j,-1j):
				if D+E in A:A.remove(D+E);C.append(D+E)
		B+=1
	return[[8*(A==B)for B in range(B)]for A in range(B)]