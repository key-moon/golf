def p(g):
	A={}
	for B in sum(g,[]):
		if B:A[B]=A.get(B,0)+1
	A.pop(max(A,key=A.get));return[[A]for A in sorted(A,key=A.get,reverse=True)]