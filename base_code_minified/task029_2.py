def p(A):
	E=[]
	for(H,D)in enumerate(A):
		C=0;F=0;B=1
		for G in range(1,len(D)):
			if D[G]==D[G-1]:B+=1
			else:
				if B>C:C,F=B,G-B
				B=1
		if B>C:C,F=B,len(D)-B
		if C>1:E.append((H,F,C))
	I=max(A[2]for A in E);J,K=[A for A in E if A[2]==I];L,M,N=J;O,P,N=K;return[A[M+1:P]for A in A[L+1:O]]