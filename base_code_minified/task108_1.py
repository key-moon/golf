def p(g):
	A=len(g)*2//5;B=[[0]*A*5 for B in[0]*A*5]
	for(E,F)in enumerate(g):
		for(G,C)in enumerate(F):
			if C:
				H=E//2*A;D=G//2*A
				for I in range(A):B[H+I][D:D+A]=[C]*A
	return B