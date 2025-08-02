def p(A):
	F=[];D=[];H=None
	for(G,B)in enumerate(A):
		for(E,C)in enumerate(B):
			if C and(G<1 or A[G-1][E]!=C)and(E<1 or B[E-1]!=C):F.append((G,E,C))
	F.sort()
	for(I,K,C)in F:
		if I!=H:D+=[[]];H=I
		D[-1]+=[C]
	J=max(len(A)for A in D)
	for B in D:B+=[B[-1]]*(J-len(B))
	return D