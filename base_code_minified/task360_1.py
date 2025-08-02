def p(A):
	C=[]
	for B in A:D=B.index(5);E=[A for A in B[:D]if A];F=[A for A in B[D+1:]if A][::-1];G=E if len(E)>=len(F)else F;C.append([0]*(4-len(G))+G)
	return C