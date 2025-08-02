def p(A):
	H=[A for B in A for A in B if A];D=next(A for A in set(H)if H.count(A)==1)
	for(J,I)in enumerate(A):
		if D in I:B,C=J,I.index(D);break
	K=sum(A[B][C]==0 for B in range(B));L=sum(A[B][C]==0 for B in range(B+1,len(A)));M=sum(A[B][C]==0 for C in range(C));N=sum(A[B][C]==0 for C in range(C+1,len(A[0])));G=max((K,'u'),(L,'d'),(M,'l'),(N,'r'))[1]
	if G=='u':
		for E in range(B):
			if A[E][C]==0:A[E][C]=D
	if G=='d':
		for E in range(B+1,len(A)):
			if A[E][C]==0:A[E][C]=D
	if G=='l':
		for F in range(C):
			if A[B][F]==0:A[B][F]=D
	if G=='r':
		for F in range(C+1,len(A[0])):
			if A[B][F]==0:A[B][F]=D
	return A