def p(A):
	H=[]
	for(B,O)in enumerate(A):
		for(C,G)in enumerate(O):
			if G:H.append((C,B,G))
	for(C,B,G)in H:
		for K in(-1,0,1):
			for L in(-1,0,1):A[B+K][C+L]=G if L|K else 5
	M={};N={}
	for(C,B,P)in H:M.setdefault(C,[]).append(B);N.setdefault(B,[]).append(C)
	for(I,D)in M.items():
		if len(D)==2:
			E,J=sorted(D)
			for F in range(E+1,J):
				if F-E&1:A[F][I]=5
	for(I,D)in N.items():
		if len(D)==2:
			E,J=sorted(D)
			for F in range(E+1,J):
				if F-E&1:A[I][F]=5
	return A