def p(g):
	C=len(g);D=len(g[0])
	for F in range(1,C+1):
		if C%F:continue
		for G in range(1,D+1):
			if D%G:continue
			E=1
			for A in range(C):
				for B in range(D):
					if g[A][B]and g[A][B]!=g[A%F][B%G]:E=0;break
				if not E:break
			if E:break
		if E:break
	for A in range(C):
		for B in range(D):
			if not g[A][B]:g[A][B]=g[A%F][B%G]
	return g