def p(A):
	B={}
	for C in sum(A,[]):
		if C:B[C]=B.get(C,0)+1
	B.pop(max(B,key=B.get));return[[A]for A in sorted(B,key=B.get,reverse=True)]