def p(g):
	C={}
	for D in range(len(g)-2):
		for E in range(len(g[0])-2):
			F={g[D+A][E+B]for A in range(3)for B in range(3)if g[D+A][E+B]}
			if len(F)==1:A=F.pop();B=tuple((B,C)for B in range(3)for C in range(3)if g[D+B][E+C]==A);C[A,B]=C.get((A,B),0)+1
	(A,B),G=max(C.items(),key=lambda t:(t[1],t[0][0]));return[[A if(C,D)in B else 0 for D in range(3)]for C in range(3)]