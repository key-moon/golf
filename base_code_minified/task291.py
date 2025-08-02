def p(g):
	for A in{A for B in g for A in B if A}:
		B=[(B,D)for(B,C)in enumerate(g)for(D,E)in enumerate(C)if E==A];C,D=zip(*B)
		if len(B)!=(max(C)-min(C)+1)*(max(D)-min(D)+1):return[[A]]