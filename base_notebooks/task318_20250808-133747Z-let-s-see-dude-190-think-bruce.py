def p(j,A=range(4)):
	for c in A:
		for E in A:j[c][E]+=j[c+5][E]
	j=[[3 if c>0 else 0 for c in c]for c in j];return j[:4]