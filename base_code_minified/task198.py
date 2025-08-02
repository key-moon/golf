def p(A):
	E=max(map(max,A));K,L=(4,3)if E==9 else(3,4);J,F=len(A),len(A[0]);D=[[0]*F for A in A];G=[]
	for B in range(J):
		for C in(0,F-1):
			if A[B][C]!=E and not D[B][C]:D[B][C]=1;G.append((B,C))
	for C in range(F):
		for B in(0,J-1):
			if A[B][C]!=E and not D[B][C]:D[B][C]=1;G.append((B,C))
	while G:
		B,C=G.pop()
		for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
			H,I=B+M,C+N
			if 0<=H<J and 0<=I<F and A[H][I]!=E and not D[H][I]:D[H][I]=1;G.append((H,I))
	for B in range(J):
		for C in range(F):
			if A[B][C]!=E:A[B][C]=K if D[B][C]else L
	return A