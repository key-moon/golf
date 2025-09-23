def p(a):
	C=None;F,G=len(a),len(a[0]);D=[(lambda s:next(iter(s))if len(s)<=1 else C)({A for A in A if A})for A in a];E=[(lambda s:next(iter(s))if len(s)<=1 else C)({a[B][A]for B in range(F)if a[B][A]})for A in range(G)]
	def H(v):
		B=[];C=0
		for A in range(1,len(v)+1):
			if A==len(v)or v[A]!=v[A-1]:B.append((C,A-1));C=A
		return B
	if all(A is not C for A in D)and len(set(D))>1:
		for(I,J)in H(D):
			for A in range(G):
				if any(a[B][A]==0 for B in range(I,J+1)):
					for B in range(I,J+1):a[B][A]=0
		return a
	if all(A is not C for A in E)and len(set(E))>1:
		for(K,L)in H(E):
			for B in range(F):
				if any(a[B][A]==0 for A in range(K,L+1)):
					for A in range(K,L+1):a[B][A]=0
	return a
