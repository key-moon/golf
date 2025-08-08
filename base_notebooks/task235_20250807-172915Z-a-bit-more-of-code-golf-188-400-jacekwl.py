def p(g,H=range):
	if not g:return[]
	J,D=len(g),len(g[0]);C=[-1]+[A for A in H(D)if all(g[B][A]==0 for B in H(J))]+[D];B=[]
	for E in H(len(C)-1):
		F,G=C[E]+1,C[E+1]
		if F>=G:continue
		A=[A[F:G]for A in g];I=sum(A.count(0)for A in A)
		if I==0:B+=[2]
		elif I==4:
			if A[1][1]==A[1][2]==A[2][1]==A[2][2]==0:B+=[8]
			elif A[1][0]==A[1][3]==A[2][0]==A[2][3]==0:B+=[3]
			elif A[2][1]==A[2][2]==A[3][1]==A[3][2]==0:B+=[4]
	return[[A]*3 for A in B]