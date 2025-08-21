def p(j):
	A=range;c,E=len(j),len(j[0]);k={}
	for W in A(c):
		for l in A(E):
			if j[W][l]:k[j[W][l]]=k.get(j[W][l],[]);k[j[W][l]].append((W,l))
	J=[C[:]for C in j]
	for(a,C)in k.items():
		if len(C)==2:
			if C[0][0]==C[1][0]:
				for l in A(min(C[0][1],C[1][1]),max(C[0][1],C[1][1])+1):J[C[0][0]][l]=a
	for(a,C)in k.items():
		if len(C)==2:
			if C[0][1]==C[1][1]:
				for W in A(min(C[0][0],C[1][0]),max(C[0][0],C[1][0])+1):J[W][C[0][1]]=a
	return J