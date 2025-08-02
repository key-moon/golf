def p(A):
	B=[]
	for E in A:
		C=E[0];D=[C]
		for F in E[1:]:
			if F!=C:D+=[(C:=F)]
		if not(B and D==B[-1]):B+=[D]
	return B