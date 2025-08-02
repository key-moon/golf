def p(g):
	D=[A for(B,A)in sorted((C,A)for B in g for(C,A)in enumerate(B)if A)];B=[]
	for A in range(3):C=D[A*3:A*3+3];B.append(((C[::-1]if A&1 else C)+[0]*3)[:3])
	return B