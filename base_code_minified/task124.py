def p(G):
	B,H=len(G),len(G[0])
	for A in G:
		for I in A:
			if I:E=I;break
		else:continue
		break
	C=B
	for(J,A)in enumerate(G):
		D=[A for(A,B)in enumerate(A)if B==E]
		if len(D)>1:C=J;break
		if D and C==B:C=J
	F=(B-C)%2==0
	for L in range(B,H):
		A=[0]*H
		if F:
			for K in D:A[K]=E
		else:A[D[-1]]=E
		G.append(A);F=not F
	return G