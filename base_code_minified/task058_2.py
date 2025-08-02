def p(A):
	G,H=len(A),len;I=H(A[0]);D=E=B=0;J=[(0,1),(1,0),(0,-1),(-1,0)]
	while 1:
		C=(I if B%2<1 else G-1)-2*(B//2)
		if C<1:break
		K,L=J[B%4]
		for F in range(C):A[D][E]=3;D+=K*(F<C-1);E+=L*(F<C-1)
		B+=1
	return A