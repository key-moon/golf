def p(A):
	O=[A[:]for A in A];J=len(A);K=len(A[0]);D={(B,C)for B in range(J)for C in range(K)if A[B][C]==5}
	for(B,C)in D:A[B][C]=0
	while D:
		E={D.pop()};H=[*E]
		while H:
			B,C=H.pop()
			for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
				F,G=B+P,C+Q
				if(F,G)in D:D.remove((F,G));E.add((F,G));H.append((F,G))
		L={(A+C,B+D)for(A,B)in E for(C,D)in((1,0),(-1,0),(0,1),(0,-1))if 0<=A+C<J and 0<=B+D<K and O[A+C][B+D]==2};M={A for(A,B)in L};R={A for(B,A)in L}
		if len(M)==1:N,I=0,M.pop()
		else:N,I=1,R.pop()
		for(B,C)in E:
			if N:A[B][2*I-C]=5
			else:A[2*I-B][C]=5
	return A