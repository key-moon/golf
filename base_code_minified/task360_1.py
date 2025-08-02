def p(g):
	B=[]
	for A in g:C=A.index(5);D=[A for A in A[:C]if A];E=[A for A in A[C+1:]if A][::-1];F=D if len(D)>=len(E)else E;B.append([0]*(4-len(F))+F)
	return B