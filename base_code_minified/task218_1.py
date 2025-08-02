def p(val_g):
	G=val_g;E=[];C=[];H=None
	for(F,A)in enumerate(G):
		for(D,B)in enumerate(A):
			if B and(F<1 or G[F-1][D]!=B)and(D<1 or A[D-1]!=B):E.append((F,D,B))
	E.sort()
	for(I,K,B)in E:
		if I!=H:C+=[[]];H=I
		C[-1]+=[B]
	J=max(len(A)for A in C)
	for A in C:A+=[A[-1]]*(J-len(A))
	return C