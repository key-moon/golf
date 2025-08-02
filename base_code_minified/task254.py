def p(A):
	H,I=len(A),len(A[0]);F=[[0]*I for A in A];E=[]
	for D in range(I):
		B=0
		for C in range(H):
			if A[C][D]==5:B+=1
			elif B:E+=B,D,C-B;B=0
		if B:E+=B,D,H-B
	J=max(E)[0];K=min(E)[0]
	for(B,D,C)in E:
		if B==J:
			for G in range(C,C+B):F[G][D]=1
		elif B==K:
			for G in range(C,C+B):F[G][D]=2
	return F