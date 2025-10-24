def p(n,r=len,g=range):
	for r in g(4):
		for A in g(4):
			if n[r][A]==0:n[r][A]=n[r][A+5]
			if n[r][A]==0:n[r][A]=n[r+5][A]
			if n[r][A]==0:n[r][A]=n[r+5][A+5]
	return[A[:4]for A in n[:4]]