def p(g,L=len,R=range):
	G,H=L(g),L(g[0]);B,E=[],0
	for C in R(G-2):
		for A in R(H-2):
			D=g[C][A:A+3]+g[C+1][A:A+3]+g[C+2][A:A+3];F=D.count(1)+D.count(8)/10
			if F>E:B=D[:];E=F
	return[B[:3],B[3:6],B[6:]]