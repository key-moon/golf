def p(g):
	A={}
	for B in sum(g,[]):A[B]=A.get(B,0)+1
	C=sorted(A.items(),key=lambda x:(-x[1],x[0]));return[[B if C>A else 0 for(B,C)in C]for A in range(C[0][1])]