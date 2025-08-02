def p(g):
	if len(set(sum(g,[])))<2:return[[5]*3]+[[0]*3]*2
	B=len({g[0][2],g[1][1],g[2][0]})>len({g[0][0],g[1][1],g[2][2]});return[[5 if C==(A,2-A)[B]else 0 for C in range(3)]for A in range(3)]