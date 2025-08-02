def p(A):
	F,G=len(A),len(A[0]);E={}
	for H in range(F):
		for I in range(G):
			J=A[H][I]
			if J:E.setdefault(J,[]).append((H,I))
	P=max(E,key=lambda I:len(E[I]));K=min(E,key=lambda I:len(E[I]));L,M=E[K][0]
	for(N,O)in((1,1),(1,-1),(-1,1),(-1,-1)):
		B=1
		while True:
			C,D=L+N*B,M+O*B
			if C<0 or D<0 or C>=F or D>=G:break
			if A[C][D]==P:
				B+=1
				while True:
					C,D=L+N*B,M+O*B
					if C<0 or D<0 or C>=F or D>=G:break
					A[C][D]=K;B+=1
				break
			B+=1
	return A