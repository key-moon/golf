def p(j):
	A=min(len(j),len(j[0]));B,C=[B[:A]for B in j[:A]],[B[-A:]for B in j[-A:]]
	if any(max(A)==8 for A in B):B,C=C,B
	return[[B[D//A][E//A]*C[D%A][E%A]//8 for E in range(A*A)]for D in range(A*A)]