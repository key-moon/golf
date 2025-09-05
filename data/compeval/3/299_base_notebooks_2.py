def p(j,A=len,c=range):
	E,k=A(j),A(j[0])
	for W in c(E):
		if j[W][0]==2 or j[W][-1]==2:
			for l in c(k):
				if j[W][l]==0:j[W][l]=2
				elif j[W][l]!=2:j[W][l]=4
	for l in c(k):
		if j[0][l]==8 or j[-1][l]==8:
			for W in c(E):
				if j[W][l]==0:j[W][l]=8
				elif j[W][l]!=8:j[W][l]=4
	return j