def p(g):
	C=len({*g[0]})>1;E=g[0]if C else[A[0]for A in g];A=[];D=None
	for B in E:
		if B!=D:A+=[B];D=B
	return C and[A]or[[A]for A in A]