def p(A):
	B=len(A)*2//5;C=[[0]*B*5 for A in[0]*B*5]
	for(F,G)in enumerate(A):
		for(H,D)in enumerate(G):
			if D:
				I=F//2*B;E=H//2*B
				for J in range(B):C[I+J][E:E+B]=[D]*B
	return C