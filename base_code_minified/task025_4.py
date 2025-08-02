def p(A):
	for G in{A for B in A for A in B if A}:
		D=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==G];H=[A for(A,B)in D];I=[A for(B,A)in D];E=max(set(H),key=H.count);F=max(set(I),key=I.count)
		if H.count(E)>I.count(F):
			for(B,C)in D:
				if B!=E:A[E+(1 if B>E else-1)][C]=G;A[B][C]=0
		else:
			for(B,C)in D:
				if C!=F:A[B][F+(1 if C>F else-1)]=G;A[B][C]=0
	return A