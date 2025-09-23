def p(g,L=len,R=range):
	E,F=L(g),L(g[0])
	for B in R(E-1):
		for A in R(F-1):
			C=g[B][A:A+2]+g[B+1][A:A+2];G=C.count(0)
			if G==1:
				for D in R(1,10):
					if C.count(D)==3:return[[D]]